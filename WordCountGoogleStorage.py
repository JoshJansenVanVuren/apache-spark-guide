# Author: Joshua Jansen Van Vueren
# Date: 2 Dec 2019
# Desc: Implementing data processing via GCP tools

'''
RUNNING THE APPLICATION:
gcloud dataproc jobs submit pyspark WordCountGoogleStorage.py \
    --cluster=${CLUSTER} \
    -- gs://${BUCKET_NAME}/input/ gs://${BUCKET_NAME}/output/
'''

import pyspark
import sys

if len(sys.argv) != 3:
    raise Exception("Exactly 2 arguments are required: <inputUri> <outputUri>")

inputUri = sys.argv[1]
outputUri = sys.argv[2]

sc = pyspark.SparkContext()
lines = sc.textFile(sys.argv[1])
words = lines.flatMap(lambda line: line.split())
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(
    lambda count1, count2: count1 + count2)
wordCounts.saveAsTextFile(sys.argv[2])
