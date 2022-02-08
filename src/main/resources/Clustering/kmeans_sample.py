from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.sql import SparkSession

spark = spark = SparkSession.builder.appName("kmeans").getOrCreate()
# Load data set
dataset = spark.read.format("libsvm").option("numFeatures","3").load("sample_kmeans_data.txt")
dataset.show()
final_dataset = dataset.select('features')
final_dataset.show()
# Create KMeans model
kmeans = KMeans().setK(3).setSeed(1)
# Fit model
model = kmeans.fit(final_dataset)
# Show centers
centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)
# Make prediction
predictions = model.transform(final_dataset)
predictions.show()
# Evaluate clustering by computing Silhouette score
evaluator = ClusteringEvaluator()
silhouette = evaluator.evaluate(predictions)
print("Silhouette with square euclidean distance =" + str(silhouette))


