package com.normanlimxk.SparkML.Clustering

import com.normanlimxk.SparkML.SparkSessionWrapper
import org.apache.spark.ml.clustering.KMeans
import org.apache.spark.ml.evaluation.ClusteringEvaluator
import org.apache.spark.sql.functions.col

object KmeansSample extends SparkSessionWrapper {
  def main(args: Array[String]): Unit = {

    // Load data set
    val dataset = spark.read
      .format("libsvm")
      .option("numFeatures", "3")
      .load("src/main/resources/Clustering/sample_kmeans_data.txt")
    dataset.show(truncate = false)
    val finalDataset = dataset.select(col("features"))
    finalDataset.show(truncate = false)

    // Create Kmeans model
    // Pre-defined no of clusters set at 3
    // Use an elbow plot to find the optimal no of clusters
    val kmeans = new KMeans()
      .setK(3)
      .setSeed(1)

    // Fit model
    val model = kmeans.fit(finalDataset)

    // Show centers
    val centers = model.clusterCenters
    println(s"Cluster Centers:")
    centers.foreach(println)

    // Make predictions
    // Given a record's feature array, which cluster will fall under
    val predictions = model.transform(finalDataset)
    predictions.show()

    // Evaluate clustering by computing Silhouette score
    val evaluator = new ClusteringEvaluator()
    val silhouette = evaluator.evaluate(predictions)
    println(s"Silhouette with square euclidean distance = ${silhouette}")
  }
}
