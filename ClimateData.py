"""
Author: Joshua Jansen Van Vuren
Desc: Class describing an object which contains climate and temperature data
"""


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
        return ("Date: %s\nMin Temp: %i\nMax Temp: %i\nAvg Min Temp: %i\nAvg Max Temp: %i\n" % (
            self.date, self.actualMinTemp, self.actualMaxTemp, self.averageMinTemp, self.averageMaxTemp))

    def splitCSVIntoArray(self, csv):
        sSplit = csv.split(",")
        # print(sSplit)
        return sSplit

    def getMaxTemp(self):
        return self.actualMaxTemp

    def getAvgMaxTemp(self):
        return self.averageMaxTemp

    def getDate(self):
        return self.date

    def isAboveAverageMax(self):
        return self.actualMaxTemp > self.averageMaxTemp
