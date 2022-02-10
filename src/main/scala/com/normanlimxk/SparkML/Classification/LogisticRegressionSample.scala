package com.normanlimxk.SparkML.Classification

import com.normanlimxk.SparkML.SparkSessionWrapper
import org.apache.spark.ml.classification.LogisticRegression
import org.apache.spark.ml.evaluation.{BinaryClassificationEvaluator, MulticlassClassificationEvaluator}

object LogisticRegressionSample extends SparkSessionWrapper {
  def main(args: Array[String]): Unit = {
    import spark.implicits._

    // Load the training data
    val dataset = spark.read
      .format("libsvm")
      .option("numFeatures", "692")
      .load("src/main/resources/Classification/sample_libsvm_data.txt")
    dataset.show(false)

    // Split into a training set and a testing set
    val Array(trainData, testData) = dataset.randomSplit(Array(0.7, 0.3))

    // Create LogisticRegression model
    val lgrModel = new LogisticRegression()

    // Fit model with training set
    val fittedModel = lgrModel.fit(trainData)

    // Evaluate with testing set
    val predictionsAndLabels = fittedModel.evaluate(testData)
    predictionsAndLabels.predictions.show()
    predictionsAndLabels.predictions.select($"probability").show(10, false)
  }
}
