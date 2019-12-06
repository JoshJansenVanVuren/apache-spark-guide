from __future__ import print_function
"""
Tasks:
Read data from BigQuery
Do some processing on that data
Apply a model to that data
Output Results to BigQuery
"""

from pyspark.context import SparkContext
from pyspark.ml.linalg import Vectors
from pyspark.ml.clustering import KMeans
from pyspark.sql.session import SparkSession
from pyspark.sql import SparkSession

"""
How to run the code, see README for more general case:
gcloud dataproc jobs submit pyspark BigQueryToMLToBigQuery.py \
    --cluster=cluster-8035 	  \
    --jars=gs://spark-lib/bigquery/spark-bigquery-latest.jar
"""

# Converts input to a vector


def vector_from_inputs(r):
    return (r["name"], Vectors.dense(float(r["age"]),
                                     float(r["weight"]),
                                     float(r["height"])))


# Setup the spark context
sc = SparkContext()
spark = SparkSession(sc)

# Use the Cloud Storage bucket for temporary BigQuery export data used
# by the connector.
bucket = spark.sparkContext._jsc.hadoopConfiguration().get(
    'fs.gs.system.bucket')
spark.conf.set('temporaryGcsBucket', bucket)

# Read the data from BigQuery as a Spark Dataframe
bio_stats_data = spark.read.format("bigquery").option(
    "table", "bio_stats_data.bio_stats_table").load()
bio_stats_data.createOrReplaceTempView("bio_stats")

# Transform the data to the required input format
df = bio_stats_data.rdd.map(vector_from_inputs).toDF(["label",
                                                      "features"])
df.cache()

# Trains a k-means model
kMeans = KMeans().setK(2)
model = kMeans.fit(df)

# Make predictions
pred = model.transform(df)

# Saving the data to BigQuery
pred.write.format('bigquery') \
    .option('table', 'bio_stats_data.bio_stats_clustered') \
    .save()
