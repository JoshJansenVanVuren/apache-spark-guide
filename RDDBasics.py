# Author: Joshua Jansen Van Vuren
# Date: 2 Dec 2019
# Desc: Following Apache Spark RDD Basics Guide

# PySpark requires the same minor version of Python in both driver and workers

from pyspark import SparkContext, SparkConf
from pyspark.sql.functions import *


class ClimateRecord(object):

    def __init__(self, string):
        s = self.splitCSVIntoArray(string)
        self.date = s[0]
        self.actualMinTemp = int(s[1])
        self.actualMaxTemp = int(s[2])
        self.actualMeanTemp = (float(s[2])+float(s[1]))/2
        self.averageMinTemp = int(s[3])
        self.averageMaxTemp = int(s[4])

    def toString(self):
        print("Date: %s \nMin Temp: %i \nMax Temp: %i \nAvg Min Temp: %i \nAvg Max Temp: %i \n" % (
            self.date, self.actualMinTemp, self.actualMaxTemp, self.averageMinTemp, self.averageMaxTemp))

    def splitCSVIntoArray(self, csv):
        sSplit = csv.split(",")
        # print(sSplit)
        return sSplit

    def getMinTemp(self):
        return self.actualMinTemp


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

# split lines
# array = lines.map(splitCSVIntoArray)
# array.saveAsTextFile("outputs/output.txt")

# convert from lines to climate records
climateRecords = lines.map(stringToClimateData)

# print the mean temperature for the day


def printMean(x):
    #x.actualMeanTemp = (x.actualMinTemp + x.actualMaxTemp)/2
    # print(x.actualMeanTemp)
    print(x.actualMeanTemp)


climateRecords.map(printMean).take(10)

# TODO:
# filter day which
#climateRecords.reduce(lambda a, b: a + b)
