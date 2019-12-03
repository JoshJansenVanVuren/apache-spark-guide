# Author: Joshua Jansen Van Vuren
# Date: 3 Dec 2019
# Desc: Unit Testing for RDDBasics example

import unittest
from ClimateData import ClimateRecord


class TestRDDBasics(unittest.TestCase):

    def test_init(self):
        testRecord = "2015-6-1,66,89,67,88"
        testOutput = "Date: 2015-6-1\nMin Temp: 66\nMax Temp: 89\nAvg Min Temp: 67\nAvg Max Temp: 88\n"
        obj = ClimateRecord(testRecord)
        self.assertEqual(obj.toString(), testOutput, 'incorrect to string')


if __name__ == '__main__':
    unittest.main()
