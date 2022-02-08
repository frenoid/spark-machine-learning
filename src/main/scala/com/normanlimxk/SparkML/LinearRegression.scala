package com.normanlimxk.SparkML

import org.apache.spark.ml.regression.LinearRegression

object LinearRegression extends SparkSessionWrapper {
  def main(args: Array[String]): Unit = {
    // Load data
    val allData = spark.read
      .format("libsvm")
      .option("numFeatures", "10")
      .load("src/main/resources/LinearRegression/sample_linear_regression_data.txt")

    // Split into training and test data
    val Array(trainData, testData) = allData.randomSplit(Array(0.7, 0.3))
    trainData.show()
    testData.show()
    val unlabeledData = testData.select("features")
    unlabeledData.show()

    // These are the default values for featuresCol, labelCol, predictionCol
    val lr = new LinearRegression()
      .setFeaturesCol("features")
      .setLabelCol("label")
      .setPredictionCol("prediction")

    // Fit the model
    val lrModel = lr.fit(trainData)

    // Print the coefficients and intercept training data
    println(s"Coefficients: ${lrModel.coefficients}")
    println(s"Intercept: ${lrModel.intercept}")

    // Testing result
    val testResult = lrModel.evaluate(testData)
    testResult.residuals.show()
    println(s"RMSE: ${testResult.rootMeanSquaredError}")
  }
}
