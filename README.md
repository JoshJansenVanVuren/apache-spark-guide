# Ambrite Apache Spark Docs
This document outlines the required packages to run the relevant files. The objective of this task is to outline and familiarize the user with the Apache Spark Model.

## Software and Version Information
1. Apache Spark 2.4.4 (pip install pyspark)
2. Python Version 2.7.15+
3. Hadoop ??

## Running the Relevant Examples
1. If PySpark pip is installed on your environment then the applications can be run through `python {APP_NAME}.py`
2. Otherwise the code should be run through 
```
 {YOUR_SPARK_HOME}/bin/spark-submit \
  --master local[4] \
  {APP_NAME}.py
```

### Example 1 - Local Text File Read And Process (SparkQuickStart.py)
1. Ensure that the required libraries are installed.
2. Add `{YOUR_SPARK_HOME}` into the command and run the command:
```
 {YOUR_SPARK_HOME}/bin/spark-submit \
  --master local[4] \
  SparkQuickStart.py
```

## Documentation
For the description of the Apache Spark Model see
`help/guide.pdf`
