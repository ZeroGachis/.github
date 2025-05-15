#!/bin/bash
BASE_REF=$1
BACKUP_BUCKET_NAME=$2
WORKSPACE=$3
PROJECT_DIR_SUBFOLDER=$4
REPO_NAME=$5

PROJECT_DIR="${WORKSPACE}/${PROJECT_DIR_SUBFOLDER}"
REMOTE_FOLDER="${WORKSPACE}/${PROJECT_DIR_SUBFOLDER}/remote"
COMPARE_STATE="state:modified.body+1"
NB_THREADS="15"
WARN_ERROR_EXCLUDE='{"include": "all", "exclude": ["NoNodesForSelectionCriteria", "NothingToDo", "PackageMaterializationOverrideDeprecation", "LogTestResult"]}'

if [ "$BASE_REF" = "main" ]
then
  COMMAND="build"
else
  COMMAND="run"
fi

printf "\n\nRunning run-dbt-clean.sh $WORKSPACE...\n"
github_workflow/scripts/run-dbt-clean.sh $WORKSPACE $PROJECT_DIR_SUBFOLDER

# Retreive remote manifest
printf "\nRetreiving last valid manifest.json...\n"
mkdir -p $REMOTE_FOLDER
aws s3 cp s3://"${BACKUP_BUCKET_NAME}"/${REPO_NAME}/valid_manifest.json.tar.gz $REMOTE_FOLDER
tar -xzf $REMOTE_FOLDER/valid_manifest.json.tar.gz -C $REMOTE_FOLDER



# Only run models which differ from remote
printf "\nRun standard models which differ from last valid manifest.json...\n"
BUILD_STANDARD="dbt \
    --warn-error-options \"$WARN_ERROR_EXCLUDE\" \
    $COMMAND \
    --project-dir $PROJECT_DIR \
    --fail-fast \
    --defer \
    --select $COMPARE_STATE \
    --state $REMOTE_FOLDER \
    --threads $NB_THREADS \
    --exclude source:*
echo $BUILD_STANDARD
eval $BUILD_STANDARD || { echo 'Running or testing standard models failed'; exit 1; }


printf "\nRun incremental models which differ from last valid manifest.json...\n"
BUILD_INCREMENTAL="dbt \
    --warn-error-options \"$WARN_ERROR_EXCLUDE\" \
    $COMMAND \
    --project-dir $PROJECT_DIR \
    --fail-fast \
    --defer \
    --select config.materialized:incremental,$COMPARE_STATE \
    --state $REMOTE_FOLDER \
    --threads $NB_THREADS \
    --exclude source:*"
echo $BUILD_INCREMENTAL
eval $BUILD_INCREMENTAL || { echo 'Running or testing incremental models failed' ; exit 1; }
