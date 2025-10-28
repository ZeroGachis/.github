#!/bin/bash
BASE_REF=$1
BACKUP_BUCKET_NAME=$2
PROJECT_DIR=$3
REPO_NAME=$4

REMOTE_FOLDER="${PROJECT_DIR}/remote"
COMPARE_STATE="state:modified.body+1"
NB_THREADS="15"
WARN_ERROR_EXCLUDE='{"error": "all", "warn": ["NoNodesForSelectionCriteria", "NothingToDo", "PackageMaterializationOverrideDeprecation", "DeprecationsSummary", "LogTestResult"]}'

if [ "$BASE_REF" = "main" ]
then
  COMMAND="build"
  FAIL_FAST=""
else
  COMMAND="run"
  FAIL_FAST="--fail-fast"
fi

printf "\nCleaning dbt project...\n"
cd $PROJECT_DIR
dbt clean
dbt deps --project-dir $PROJECT_DIR


# Retreive remote manifest
printf "\nRetreiving last valid manifest.json...\n"
mkdir -p $REMOTE_FOLDER
aws s3 cp s3://"${BACKUP_BUCKET_NAME}"/${REPO_NAME}/valid_manifest.json.tar.gz $REMOTE_FOLDER
tar -xzf $REMOTE_FOLDER/valid_manifest.json.tar.gz -C $REMOTE_FOLDER

# Run snapshot which differ from remote
printf "\nRun snapshot models which differ from last valid manifest.json...\n"
BUILD_SNAPSHOT="dbt \
    --warn-error-options \"$WARN_ERROR_EXCLUDE\" \
    snapshot \
    --project-dir $PROJECT_DIR \
    $FAIL_FAST \
    --defer \
    --select state:modified.body \
    --state $REMOTE_FOLDER \
    --threads $NB_THREADS \
    --exclude source:* \
    --exclude elementary "
echo $BUILD_SNAPSHOT
eval $BUILD_SNAPSHOT || { echo 'Running or testing snapshot models failed'; exit 1; }


# Only run models which differ from remote and models with associated macros change
printf "\nRun standard models which differ from last valid manifest.json...\n"
BUILD_STANDARD="dbt \
    --warn-error-options \"$WARN_ERROR_EXCLUDE\" \
    $COMMAND \
    --project-dir $PROJECT_DIR \
    $FAIL_FAST \
    --defer \
    --select state:modified.macros $COMPARE_STATE \
    --state $REMOTE_FOLDER \
    --threads $NB_THREADS \
    --exclude source:* \
    --exclude elementary "
echo $BUILD_STANDARD
eval $BUILD_STANDARD || { echo 'Running or testing standard models failed'; exit 1; }


printf "\nRun incremental models which differ from last valid manifest.json...\n"
BUILD_INCREMENTAL="dbt \
    --warn-error-options \"$WARN_ERROR_EXCLUDE\" \
    $COMMAND \
    --project-dir $PROJECT_DIR \
    $FAIL_FAST \
    --defer \
    --select config.materialized:incremental,$COMPARE_STATE \
    --state $REMOTE_FOLDER \
    --threads $NB_THREADS \
    --exclude source:* \
    --exclude elementary "
echo $BUILD_INCREMENTAL
eval $BUILD_INCREMENTAL || { echo 'Running or testing incremental models failed' ; exit 1; }
