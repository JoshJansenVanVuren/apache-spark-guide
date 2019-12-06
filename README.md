# Apache Spark Guide

This document outlines the required packages and steps to run the relevant examples. The objective of this task is to outline and familiarize the user with the Apache Spark Model.

I would recommend cloning the repository locally and going through each example, all of which are relatively simple to understand. Giving a brief glance to the `help/guide.pdf` would also be advised as much of the programming model is discussed there as well as a multitude of links to different use-cases etcetera.

## Software and Version Information

1. Apache Spark 2.4.4 (pip install PySpark)
    * According to the spark documentation Spark 2.4.4 works with Python 2.7+ or Python 3.4+.
2. Python Version 3.6.8
3. Java JDK V8

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

Alteratively if PySpark pip is installed on your environment then the applications can be run through `python {APP_NAME}.py`.

`local[4]` runs the code on 4 local cores.

### Example 2 - RDD Basics (RDDBasics.py)

This is the example includes some UDF's, but still runs locally in batch, and includes some unit tests. A few filters and transformations are computed on data to show the simplicity.

1. Ensure that the required libraries are installed.
2. Clone repo and navigate to it in terminal
3. Add `{YOUR_SPARK_HOME}` into the command and run the command:

```cmd
 {YOUR_SPARK_HOME}/bin/spark-submit \
  --master local[4] \
  SparkQuickStart.py
```

BigQuery only supported in Scala [example here](https://cloud.google.com/dataproc/docs/tutorials/bigquery-connector-spark-example)

### Example 3 - DataProc and Cloud Storage (WordCountGoogleStorage.py)

This example reads a text file from a cloud storage bucket, does a simple word count on that data and outputs the word count to a text file in that same bucket

1. [Create a cluster](https://cloud.google.com/dataproc/docs/quickstarts/quickstart-explorer-create}) and note the cluster name `${CLUSTER}`.

2. Do all the correct authentication steps [getting started](https://cloud.google.com/docs/authentication/getting-started).

3. Create a bucket, note the bucket name `${BUCKET_NAME}`. inside the bucket create a folder `/input/` and upload any file that you would like word counts of.

4. Run the command, note that the cluster location may be required and requires another line in the command:

```cmd
gcloud dataproc jobs submit pyspark WordCountGoogleStorage.py \
    --cluster=${CLUSTER} \
    -- gs://${BUCKET_NAME}/input/ gs://${BUCKET_NAME}/output/
```

### Example 4 - DataProc Big Query (BigQueryExample.py)

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

### Example 5 - Big Query To K-Means to Big Query (BigQueryToMLToBigQuery.py)

This example takes input from a big query table, transforms the data into a Dataset with columns ["label","features"] and then does a K-Means Clustering algorithm on the data, writing the output to another Big Query table.

1. Create a cluster, note the bucket name `${CLUSTER_NAME}`.
2. Create a BigQuery dataset with the name `bio_stats_data`.
3. In that dataset create a table `bio_stats_table`, upload the CSV file `biostats.csv`.
4. Run the command, when the job runs, the output will be sent to the table `bio_stats_clustered`.

```cmd
gcloud dataproc jobs submit pyspark BigQueryToMLToBigQuery.py \
    --cluster=${CLUSTER_NAME}   \
    --jars=gs://spark-lib/bigquery/spark-bigquery-latest.jar
```

#### Findings

* Data must be in a Dataset when working in certain libraries.
* Dataset must have column with name "Features" when training certain models.
* A temporary google storage bucket must be set.
* There are two different available ML libraries `spark.ml` and `spark.mllib`.
* There a multitude of available models in the libraries and implementing them requires minimal code.

### Example 6 - Streaming Word Count (StreamingWordCountGoogleStorage.py)

This example checks for new text files in a Google Storage Bucket, batches data based of a specified window, does a word count on the DStream and writes the data to another bucket in Google Storage

1. ${CLUSTER}
2. Create input and output buckets, note the bucket names `${BUCKET_NAME_IN}` and `${BUCKET_NAME_OUT}`, create a folder on the input bucket, and once the job is running upload a file of your choice.
3. Run the command:

```cmd
gcloud dataproc jobs submit pyspark StreamingWordCountGoogleStorage.py \
    --cluster=${CLUSTER_NAME} \
    -- gs://${BUCKET_NAME_IN}/input/ gs://${BUCKET_NAME_OUT}/output/
```

## Documentation

For a more abstract discussion of the Apache Spark Model see `help/guide.pdf`

## Other Files

`ClimateData.py` structure to hold read in climate data

`test.py` unit testing (no pipeline based tests implemented)
