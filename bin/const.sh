#!/usr/bin/env bash
declare -i MajorVersion=0
declare -i MinorVersion=0
declare -i PatchVersion=1
declare -x PipelineVersion=${MajorVersion}.${MinorVersion}.${PatchVersion}

declare -x PipelineName="Pipeline Name Goes Here"

declare -x DefaultAnnotationDir=/ref/refGenomes
declare -x DefaultMinimapIndexDir=/ref/minimap2Index
declare -x DefaultBwaIndexDir=/ref/bwaIndex

declare -x S3FastqLocation=s3://intellia-basespace/run_data

declare -x DefaultProductionDB=metadata.db.ampliconseq.com
declare -x DefaultDevDb=development.metadata.db.ampliconseq.com

declare -x SendEmailAddr=informatics_pipeline@intelliatx.com
declare -x DEFAULT_CONTACT=bo.han@intelliatx.com
declare -x ERROR_CONTACT=bo.han@intelliatx.com

declare -x Default3PrimerAdapter=AGATCGGAAGAGCACACGTCT
