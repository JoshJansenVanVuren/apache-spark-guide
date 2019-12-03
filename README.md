# Apache Spark Guide

This document outlines the required packages to run the relevant files. The objective of this task is to outline and familiarize the user with the Apache Spark Model.

## Software and Version Information

1. Apache Spark 2.4.4 (pip install pyspark)
    * According to the spark documentation Spark 2.4.4 works with Python 2.7+ or Python 3.4+.
2. Python Version 3.6.8
3. Hadoop ??

## Running the Relevant Examples

1. If PySpark pip is installed on your environment then the applications can be run through `python {APP_NAME}.py`
2. Otherwise the code should be run through
3. `local[4]` runs the code on 4 cores.

```cmd
{YOUR_SPARK_HOME}/bin/spark-submit \
--master local[4] \
{APP_NAME}.py
```

### Example 1 - Local Text File Read And Process (SparkQuickStart.py)

This is the most basic example, and uses not UDF's.

1. Ensure that the required libraries are installed.
2. Clone repo and navigate to it in terminal
3. Add `{YOUR_SPARK_HOME}` into the command and run the command:

```cmd
 {YOUR_SPARK_HOME}/bin/spark-submit \
  --master local[4] \
  SparkQuickStart.py
```

### Example 2 - RDD Basics (RDDBasics.py)

This is the example includes some UDF's, but still runs locally in batch, and includes some unit tests. A few filters and transformations are computed on data to show the simplticity.

1. Ensure that the required libraries are installed.
2. Clone repo and navigate to it in terminal
3. Add `{YOUR_SPARK_HOME}` into the command and run the command:

```cmd
 {YOUR_SPARK_HOME}/bin/spark-submit \
  --master local[4] \
  SparkQuickStart.py
```


## Documentation

For the description of the Apache Spark Model see
`help/guide.pdf`

## File Descriptions

`ClimateData.py` structure to hold read in climate data
`test.py` unit testing
`SparkQuickStart.py` most basic implementation of spark structure
`RDDBasics.py` spark implementation with UDF's and unit tests
