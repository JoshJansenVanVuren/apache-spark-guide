# Author: Joshua Jansen Van Vuren
# Date: 2 Dec 2019
# Desc: Following Apache Spark quick start guide

'''
RUNNING THE APPLICATION:
 YOUR_SPARK_HOME/bin/spark-submit \
  --master local[4] \
  sparkQuickStart.py
'''

# SparkSession used to create Datasets
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Name of file to read from
textFile = "biostats.csv"

# Create session
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

# Primary abstraction is Dataset (collection of items)
logData = spark.read.text(textFile).cache() # Data can be cached in spark

# Count the number of lines with M and F
numMs = logData.filter(logData.value.contains('M')).count()
numFs = logData.filter(logData.value.contains('F')).count()
numLines = logData.count()

print("Lines with M: %i, lines with F: %i" % (numMs, numFs))
print("Lines in file: %i" % (numLines))

# Count the number of words in each line
maxWords = logData.select(size(split(logData.value, "\s+")).name("numWords")).agg(max(col("numWords"))).collect()

print("\nMax Number Words:")
print(maxWords)

spark.stop()
