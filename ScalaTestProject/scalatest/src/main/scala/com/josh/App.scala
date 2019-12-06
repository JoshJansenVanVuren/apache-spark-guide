package com.josh

import org.apache.spark.sql.SparkSession

/**
 * @author Joshua Jansen Van Vuren
 * mvn package
 * mvn scala:run -DmainClass=com.josh.App
 */
object App {
  def main(args: Array[String]) {
    // Get the text file name
    val logFile = "skrip_input.txt"

    // Start the Spark session
    val spark = SparkSession.builder()
                            .appName("Scala Spark Basic Example")
                            .config("spark.master", "local")
                            .getOrCreate()
    
    // Read in the file
    val logData = spark.read.textFile(logFile).cache()

    // Some functions to count the number of lines that contain a's or b's
    val numAs = logData.filter(line => line.contains("a")).count()
    val numBs = logData.filter(line => line.contains("b")).count()

    // Print the outputs
    println(s"Lines with a: $numAs, Lines with b: $numBs")
    spark.stop()
  }
}
