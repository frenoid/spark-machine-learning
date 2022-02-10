package com.normanlimxk.SparkML.Classification

import com.normanlimxk.SparkML.SparkSessionWrapper
import org.apache.spark.ml.classification.LogisticRegression
import org.apache.spark.ml.feature.{VectorAssembler, VectorIndexer, OneHotEncoder, StringIndexer}
import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.evaluation.BinaryClassificationEvaluator

object LogisticRegressionTitanic extends SparkSessionWrapper {
  def main(args: Array[String]): Unit = {
    import spark.implicits._

    // Load dataset
    val data = spark.read
      .option("inferSchema", "true")
      .option("header", "true")
      .csv("src/main/resources/Classification/titanic.csv")
    data.printSchema()
    println(data.columns)

    // Select numeric columns and categorical columns
    val numericCols = data.select($"Survived", $"Pclass", $"Sex", $"Age", $"SibSp", $"Parch", $"Fare", $"Embarked")
    val finalData = numericCols.na.drop()
    finalData.show()

    // Working with categorical columns
    // There are transformers which will be used in the upcoming pipeline
    // Transforms implement a method called which takes one dataframe and output another
    val genderIndexer = new StringIndexer().setInputCol("Sex").setOutputCol("SexIndex")
    val genderEncoder = new OneHotEncoder().setInputCol("SexIndex").setOutputCol("SexVec")
    val embarkIndexer = new StringIndexer().setInputCol("Embarked").setOutputCol("EmbarkIndex")
    val embarkEncoder = new OneHotEncoder().setInputCol("EmbarkIndex").setOutputCol("EmbarkVec")
    val asesembler = new VectorAssembler()
      .setInputCols(Array("Pclass", "SexVec", "Age", "SibSp", "Parch", "Fare","EmbarkVec"))
      .setOutputCol("features")

    // Create a logistic regression model
    // models are estimators
    // Estimators implement the method fit which creates Transforms
    val logRegTitanic = new LogisticRegression()
      .setFeaturesCol("features")
      .setLabelCol("Survived")

    // Create a pipeline
    // A pipeline combines a series of Transformers and Estimators through which data can be run
    val pipeline = new Pipeline()
      .setStages(Array(genderIndexer, embarkIndexer, genderEncoder, embarkEncoder, asesembler, logRegTitanic))

    // Split the data
    val Array(trainTitanicData, testTitanicData) = finalData.randomSplit(Array(0.7, 0.3))

    // Fit the model on the training data
    val fitModel = pipeline.fit(trainTitanicData)

    // Use the model to transform the test data
    val results = fitModel.transform(testTitanicData)

    // Evaluate the results
    val evaluation = new BinaryClassificationEvaluator()
      .setRawPredictionCol("prediction")
      .setLabelCol("Survived")
    results.select($"Survived", $"prediction").show(30)
    val AUC = evaluation.evaluate(results)
    println(s"AUC is $AUC")
  }
}
