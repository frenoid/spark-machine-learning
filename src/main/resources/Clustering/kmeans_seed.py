from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans

spark = SparkSession.builder.appName('kmeans').getOrCreate()
# Load data set
dataset = spark.read.csv("seeds_dataset.csv",header=True,inferSchema=True)
dataset.head(1)
# Show statistics
dataset.describe().show()
# Format the data
from pyspark.ml.feature import VectorAssembler
dataset.columns
assembler = VectorAssembler(inputCols= dataset.columns,outputCol='features')
final_data = assembler.transform(dataset)
final_data.printSchema()
# Scale the data
# It is good to scale our data to deal with the curse of dimensionality
from pyspark.ml.feature import StandardScaler
scaler = StandardScaler(inputCol="features",outputCol="scaledFeatures")
# Compute summary statistics by fitting StandardScaler
scalerModel = scaler.fit(final_data)
# Normalize each feature to hae unit standard deviation
final_data = scalerModel.transform(final_data)
# Train the model and evaluate
kmeans = KMeans(featuresCol='scaledFeatures', k=3)
model = kmeans.fit(final_data)
# Shows the results
centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)

model.transform(final_data).select('prediction').show()
