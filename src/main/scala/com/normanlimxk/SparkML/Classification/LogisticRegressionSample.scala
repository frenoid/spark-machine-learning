package com.normanlimxk.SparkML.Classification

import com.normanlimxk.SparkML.SparkSessionWrapper
import org.apache.spark.ml.classification.LogisticRegression
import org.apache.spark.ml.evaluation.{BinaryClassificationEvaluator, MulticlassClassificationEvaluator}

object LogisticRegressionSample extends SparkSessionWrapper {
  def main(args: Array[String]): Unit = {
    // Load the training data
    val dataset = spark.read
      .format("libsvm")
      .option("numFeatures", "692")
      .load("src/main/resources/Classification/sample_libsvm_data.txt")
    dataset.show(false)

    // To be continued
  }

}
