package com.josh

import org.apache.spark.sql.SparkSession

/**
 * @author Joshua Jansen Van Vuren
 * mvn package
 * mvn scala:run -DmainClass=com.josh.App
 */
object App {
  
  def foo(x : Array[String]) = x.foldLeft("")((a,b) => a + b)
  
  def main(args: Array[String]) {
    val logFile = "skrip_input.txt" // Should be some file on your system
    val spark = SparkSession
                                      .builder()
                                      .appName("Scala Spark Basic Example")
                                      .config("spark.master", "local")
                                      .getOrCreate();
    val logData = spark.read.textFile(logFile).cache()
    val numAs = logData.filter(line => line.contains("a")).count()
    val numBs = logData.filter(line => line.contains("b")).count()
    println(s"Lines with a: $numAs, Lines with b: $numBs")
    spark.stop()
  }

}
