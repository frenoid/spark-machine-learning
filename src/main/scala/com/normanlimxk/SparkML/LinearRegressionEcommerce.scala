package com.normanlimxk.SparkML

import org.apache.spark.ml.regression.LinearRegression
import org.apache.spark.ml.linalg.Vector
import org.apache.spark.ml.feature.VectorAssembler

object LinearRegressionEcommerce extends SparkSessionWrapper {
  def main(args: Array[String]): Unit = {

    // Load data into dataframe
    val data = spark.read
      .option("inferSchema", "true")
      .option("header", "true")
      .csv("src/main/resources/LinearRegression/Ecommerce_Customers.csv")
    import spark.implicits._

    // Print the Dataframe's schema
    data.printSchema()
    data.show()
    println(data.head())

    // Set up the Dataframe for Machine Learning
    println(data.columns)

    // We need to change the data into two columns named "label" and "features
    // We will use only numeric columns as features
    val assembler = new VectorAssembler()
      .setInputCols(Array("Avg Session Length", "Time on App", "Time on Website", "Length of Membership"))
      .setOutputCol("features")
    val output = assembler.transform(data)
    output.select($"features").show(false)
    output.show(false)

    // Our final dataset has two columns "features" and "Yearly Amount Spent"
    val finalData = output.select($"features", $"Yearly Amount Spent")

    // Split into training and testing datasets
    val Array(trainData, testData) = finalData.randomSplit(Array(0.7, 0.3))
    trainData.describe().show()
    testData.describe().show()

    // Create a linear regression model object
    val lr = new LinearRegression()
      .setLabelCol("Yearly Amount Spent")

    // Fit the model to the data and name this model lrModel
    val lrModel = lr.fit(trainData)

    // Print the coefficients and intercept for linear regression
    println(s"Coefficients: ${lrModel.coefficients} Intercept: ${lrModel.intercept}")

    // Evaluate the model on a test dataset
    val testResult = lrModel.evaluate(testData)
    testResult.residuals.show()
    println(s"RMSE: ${testResult.rootMeanSquaredError}")
    println(s"MSE: ${testResult.meanSquaredError}")
  }
}
