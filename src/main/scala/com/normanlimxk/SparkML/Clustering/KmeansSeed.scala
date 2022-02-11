package com.normanlimxk.SparkML.Clustering

import com.normanlimxk.SparkML.SparkSessionWrapper
import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.feature.VectorAssembler
import org.apache.spark.ml.feature.StandardScaler
import org.apache.spark.ml.clustering.KMeans

object KmeansSeed extends SparkSessionWrapper {
  def main(args: Array[String]): Unit = {

    // Load data set
    val dataset = spark.read
      .option("header", "true")
      .option("inferSchema", "true")
      .csv("src/main/resources/Clustering/seeds_dataset.csv")
    dataset.show(1, false)

    // Show statistics
    dataset.describe().show()

    // Format the data
    dataset.columns.foreach(println)
    val vecAssember = new VectorAssembler()
      .setInputCols(dataset.columns)
      .setOutputCol("features")
    val vectorizedData = vecAssember.transform(dataset)

    // Scale the data to deal with the curse of dimensionality
    // StandardScaler transforms a dataset of Vector rows, normalizing each feature to have unit standard deviation and/or zero mean.
    val scaler = new StandardScaler()
      .setInputCol("features")
      .setOutputCol("scaledFeatures")
      .setWithStd(true) // scale the data to unit standard deviation
      .setWithMean(false) // do not center the mean

    // Compute summary statistics by fitting StandardScaler
    val scalerModel = scaler.fit(vectorizedData)

    // Normalize each feature to have unit standard deviation
    val normalizedData = scalerModel.transform(vectorizedData)

    // Train the model and evaluate
    // predefined no of clusters is 3
    val kmeans = new KMeans()
      .setFeaturesCol("scaledFeatures")
      .setK(3)
    val model = kmeans.fit(normalizedData)

    // Show results
    val centers = model.clusterCenters
    println("Cluster Centers:")
    centers.foreach(println)

    model.transform(normalizedData).select("prediction").show(truncate = false)
  }
}
