# Apache Spark Guide

This document outlines the required packages, and provides a step-by-step guide to run the different PySpark examples. The objective of this task is to outline and familiarize the user with the Apache Spark Model.

I would recommend cloning the repository locally and going through each example, all of which are relatively simple to understand. A brief glance at `help/guide.pdf` would also be advised as much of the programming model is discussed. A multitude of links to different use-cases etcetera are also available in that document.

## PySpark Software and Version Information

1. Apache Spark 2.4.4 (pip install PySpark)
    * According to the spark documentation Spark 2.4.4 works with Python 2.7+ or Python 3.4+.
2. Python Version 3.6.8
3. Java JDK V8
4. It's useful to have a virtual environment to not mess with other system dependencies:

```cmd
pip install virtualenv
virtualenv -p {PATH_TO_PYTHON_INSTALL} venv
source venv/bin/activate
```

## Scala Software and Version Information

Initially I ran Scala using sbt on Ubuntu, this is quite convoluted however, because to build and deploy the project I used Maven, which I was more familiar with.

There are really only two installations required:

1. Maven `apt-get install maven`
2. Java JDK 8 (Scala can run newer versions, but PySpark cannot)

Recommendations to get used to the Scala Environment:

1. I would recommend trying the scala hello world example [here](https://docs.scala-lang.org/getting-started/sbt-track/getting-started-with-scala-and-sbt-on-the-command-line.html), this example uses sbt
2. Further I would recommend, especially if you've never set up a scala maven project, following this [example](https://docs.scala-lang.org/tutorials/scala-with-maven.html) which gives a very neat method to setup new Scala Maven projects.

## PySparkExamples

### Example 1 - Local Text File Read And Process (SparkQuickStart.py)

This is the most basic example, and uses not UDF's.

1. Ensure that the required libraries are installed (`requirements.txt`)
2. Clone repo locally and navigate to it in a terminal
3. Add `{YOUR_SPARK_HOME}` into the command and run the command:

```cmd
 {YOUR_SPARK_HOME}/bin/spark-submit \
  --master local[4] \
  SparkQuickStart.py
```

Alteratively if PySpark pip is installed on your environment then the applications can be run through

```cmd
python {APP_NAME}.py
```

* `local[4]` runs the code on 4 local cores.

### Example 2 - RDD Basics (RDDBasics.py)

This is the example includes some UDF's, but still runs locally and in batch, and includes some unit tests. A few filters and transformations are computed on data to highlight the simplicity.

1. Ensure that the required libraries are installed.
2. Clone repo and navigate to it in terminal
3. Add `{YOUR_SPARK_HOME}` into the command and run the command:

```cmd
 {YOUR_SPARK_HOME}/bin/spark-submit \
  --master local[4] \
  SparkQuickStart.py
```

### Example 3 - DataProc and Cloud Storage (WordCountGoogleStorage.py)

This example reads a text file from a cloud storage bucket, does a simple word count on that data and outputs the word count to a text file in that same bucket

1. [Create a cluster](https://cloud.google.com/dataproc/docs/quickstarts/quickstart-explorer-create}) and note the cluster name `${CLUSTER}`.

2. Do all the correct authentication steps [getting started](https://cloud.google.com/docs/authentication/getting-started).

3. Create a bucket, note the bucket name `${BUCKET_NAME}`. inside the bucket create a folder `/input/` and upload any file that you would like.

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

1. Create a cluster, note the cluster name `${CLUSTER_NAME}`.
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

1. Create a cluster, note the cluster name `${CLUSTER_NAME}`.
2. Create input and output buckets, note the bucket names `${BUCKET_NAME_IN}` and `${BUCKET_NAME_OUT}`, create a folder on the input bucket, and once the job is running upload a file of your choice.
3. Run the command:

```cmd
gcloud dataproc jobs submit pyspark StreamingWordCountGoogleStorage.py \
    --cluster=${CLUSTER_NAME} \
    -- gs://${BUCKET_NAME_IN}/input/ gs://${BUCKET_NAME_OUT}/output/
```

## Scala Example

1. Navigate to `ScalaTestProject/scalatest/`
2. Run the command `mvn package`
3. Run the command `mvn scala:run -DmainClass=com.josh.App`

### Notes

* The included dependencies can take different forms based on the system one uses to run the program (maven vs sbt).

MAVEN

```maven
<dependency>
    <groupId>org.apache.spark</groupId>
    <artifactId>spark-sql_2.12</artifactId>
    <version>2.4.4</version>
</dependency>
```

SBT

```sbt
libraryDependencies += "org.apache.spark" %% "spark-sql" % "2.4.4"
```

## Documentation

For a more abstract discussion of the Apache Spark Model see `help/guide.pdf`

## Other Files

`PySparkExamples/ClimateData.py` structure to hold read in climate data

`PySparkExamples/test.py` unit testing (no pipeline based tests implemented)
