# Apache Spark Guide

This document outlines the required packages and steps to run the relevant examples. The objective of this task is to outline and familiarize the user with the Apache Spark Model.

## Software and Version Information

1. Apache Spark 2.4.4 (pip install pyspark)
    * According to the spark documentation Spark 2.4.4 works with Python 2.7+ or Python 3.4+.
2. Python Version 3.6.8
3. Hadoop ??

### Example 1 - Local Text File Read And Process (SparkQuickStart.py)

This is the most basic example, and uses not UDF's.

1. Ensure that the required libraries are installed.
2. Clone repo and navigate to it in terminal
3. Add `{YOUR_SPARK_HOME}` into the command and run the command:

```cmd
 {YOUR_SPARK_HOME}/bin/spark-submit \
  --master local[4] \
  SparkQuickStart.py
```

Altenatively if PySpark pip is installed on your environment then the applications can be run through `python {APP_NAME}.py`.

`local[4]` runs the code on 4 local cores.

### Example 2 - RDD Basics (RDDBasics.py)

This is the example includes some UDF's, but still runs locally in batch, and includes some unit tests. A few filters and transformations are computed on data to show the simplticity.

1. Ensure that the required libraries are installed.
2. Clone repo and navigate to it in terminal
3. Add `{YOUR_SPARK_HOME}` into the command and run the command:

```cmd
 {YOUR_SPARK_HOME}/bin/spark-submit \
  --master local[4] \
  SparkQuickStart.py
```

BigQuery only supported in Scala [example here](https://cloud.google.com/dataproc/docs/tutorials/bigquery-connector-spark-example)

### Example 3 - Dataproc and Cloud Storage (WordCountGoogleStorage.py)

This example reads a text file from a cloud storage bucket, does a simple word count on that data and outputs the word count to a text file in that same bucket

1. [Create a cluster](https://cloud.google.com/dataproc/docs/quickstarts/quickstart-explorer-create}) and note the cluster name `${CLUSTER}`.

2. Do all the correct authentication steps [getting started](https://cloud.google.com/docs/authentication/getting-started).

3. Create a bucket, note the bucket name `${BUCKET_NAME}`. inside the bucket create a folder `/input/` and upload any file that you would like word counts of.

4. Run the command:

```cmd
gcloud dataproc jobs submit pyspark WordCountGoogleStorage.py \
    --cluster=${CLUSTER} \
    -- gs://${BUCKET_NAME}/input/ gs://${BUCKET_NAME}/output/
```

### Example 4 - Dataproc Big Query (BigQueryExample.py)

This example does a simple word count from data stored on a public big query table. Does a word count on the data and then outputs the word count to another big query table.

#### Some info

`gs://spark-lib/bigquery/spark-bigquery-latest.jar` is the jar of the connector to bigquery

1. Create a cluster, note the bucket name `${CLUSTER_NAME}`.
2. Create a BigQuery dataset with the name `wordcount_dataset`.
3. Run the command:

```cmd
gcloud dataproc jobs submit pyspark BigQueryExample.py \
    --cluster=${CLUSTER_NAME}   \
    --jars=gs://spark-lib/bigquery/spark-bigquery-latest.jar
```

## Documentation

For a more comprehensive discussion of the Apache Spark Model see `help/guide.pdf`

## File Descriptions

`ClimateData.py` structure to hold read in climate data

`test.py` unit testing

`SparkQuickStart.py` most basic implementation of spark structure

`RDDBasics.py` spark implementation with UDF's and unit tests
