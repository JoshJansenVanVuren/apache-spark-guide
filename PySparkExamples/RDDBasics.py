# Author: Joshua Jansen Van Vueren
# Date: 2 Dec 2019
# Desc: Following Apache Spark RDD Basics Guide

# PySpark requires the same minor version of Python in both driver and workers

from pyspark import SparkContext, SparkConf
from pyspark.sql.functions import *
from ClimateData import ClimateRecord

# Structure for holding the climate data records


def stringToClimateData(s):
    return ClimateRecord(s)


testRecord = "2015-6-1,66,89,67,88"
obj = ClimateRecord(testRecord)
obj.toString()

appName = "RDDBasics"
master = "local"  # in practice this should be set through spark-submit
conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)

# get external dataset file
fileName = "temp.csv"

lines = sc.textFile(fileName)
lineLengths = lines.map(lambda s: len(s))
totalLength = lineLengths.reduce(lambda a, b: a + b)
print("totalLength: %i" % (totalLength))

# write out lines - note this will fail if the text file already exists
lines.saveAsTextFile("outputs/output.txt")

# convert from lines to climate records
climateRecords = lines.map(stringToClimateData)

# print the mean temperature for the day


def printMean(x):
    print(x.getMaxTemp())


climateRecords.map(printMean).take(10)  # print only 10

# return only the max and mean max columns
onlyMaxandMeanTemp = climateRecords.map(
    lambda a: (a.getMaxTemp(), a.getAvgMaxTemp())).collect()

# print them out - note the simplicity of splitting the columns and iterating
# through the RDD
for (i, j) in onlyMaxandMeanTemp:
    print("Max: %i \nMean Max: %i" % (i, j))

# filter out the days whose max is higher than the average max
aboveAverageMax = climateRecords.filter(
    lambda x: x.isAboveAverageMax() == 1).collect()

for x in aboveAverageMax:
    print("Date: %s \tMax: %i" % (x.getDate(), x.getMaxTemp()))
