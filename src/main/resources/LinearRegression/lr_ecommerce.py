from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('lr_example').getOrCreate()
from pyspark.ml.regression import LinearRegression
# Load dataset into dataframe
data = spark.read.csv("Ecommerce_Customers.csv",inferSchema=True,header=True)
# Print the Schema of the dataframe
data.printSchema()
data.show()
data.head()
for item in data.head():
    print(item)

# Setting up DataFrame for Machine Learning
from pyspark.ml.linalg import Vector
from pyspark.ml.feature import VectorAssembler
data.columns
# We need to change the data into the form of two columns ("label", "features")
assembler = VectorAssembler(inputCols=["Avg Session Length",
"Time on App",
"Time on Website",
"Length of Membership"],
outputCol="features")
output = assembler.transform(data)
output.select("features").show()
output.show()
# Final dataset with two columns ("features", "label")
final_data = output.select("features","Yearly Amount Spent")
final_data.show()
# Split into training and testing datasets
train_data, test_data = final_data.randomSplit([0.7,0.3])
train_data.describe().show()
test_data.describe().show()
# Create a linear regression model object
lr = LinearRegression(labelCol='Yearly Amount Spent')
# Fit the model to the data and call this model lrModel
lrModel = lr.fit(train_data,)
# print the coefficients and intercept for linear regression
print("Coefficients: {} Intercept {}".format(lrModel.coefficients, lrModel.intercept))
test_result = lrModel.evaluate(test_data)
test_result.residuals.show()
print("RMSE:{}".format(test_result.rootMeanSquaredError))
print("MSE: {}".format(test_result.meanSquaredError))
