# Author: Joshua Jansen Van Vuren
# Date: 2 Dec 2019
# Desc: Implementing data processing via GCP tools

'''
RUNNING THE APPLICATION:
gcloud dataproc jobs submit pyspark StreamingWordCountGoogleStorage.py \
    --cluster=${CLUSTER} \
    -- gs://${BUCKET_NAME}/input/ gs://${BUCKET_NAME}/output/

gcloud dataproc jobs submit pyspark StreamingWordCountGoogleStorage.py \
    --cluster=cluster-8035 \
    -- gs://skripsie/input/ gs://skripsie/output/
'''

import pyspark
import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception(
            "Exactly 2 arguments are required: <inputUri> <outputUri>")

    inputUri = sys.argv[1]
    outputUri = sys.argv[2]

    sc = SparkContext(appName="PythonStreamingHDFSWordCount")
    ssc = StreamingContext(sc, 1)

    lines = ssc.textFileStream(sys.argv[1])
    words = lines.flatMap(lambda line: line.split())
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(
        lambda count1, count2: count1 + count2)
    wordCounts.saveAsTextFiles(sys.argv[2])

    ssc.start()
    ssc.awaitTermination()
