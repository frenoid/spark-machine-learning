package com.normanlimxk.SparkML

object Main extends SparkSessionWrapper {
  def main(args: Array[String]): Unit = {
    val l = spark.sparkContext.parallelize((1 to 1000).toList)
    val result = l.reduce(_ + _)
    println(result)
  }
}
