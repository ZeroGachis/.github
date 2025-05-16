#!/bin/bash
PROJECT_DIR=$1
DBT_PROFILE=$2
BACKUP_BUCKET_NAME=$3
REPO_NAME=$4


dbt compile --profile $DBT_PROFILE --project-dir $PROJECT_DIR
tar -czf $PROJECT_DIR/target/valid_manifest.json.tar.gz -C $PROJECT_DIR/target manifest.json
aws s3 cp $PROJECT_DIR/target/valid_manifest.json.tar.gz s3://$BACKUP_BUCKET_NAME/$REPO_NAME/