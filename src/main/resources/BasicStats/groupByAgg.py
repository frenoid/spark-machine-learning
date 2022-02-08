from pyspark.sql import SparkSession
# Start Spark Session
spark = SparkSession.builder.appName("groupbyagg").getOrCreate()
# Read sales data
df = spark.read.csv('sales_info.csv',inferSchema=True,header=True)
df.printSchema()
df.show()
# Group by company
df.groupBy("Company")
# Returns a GroupedData object, off of which you can all various methods
# Mean
df.groupBy("Company").mean().show()
# Count
df.groupBy("Company").count().show()
# Max
df.groupBy("Company").max().show()
# Min
df.groupBy("Company").min().show()
# Order by sales ascending
df.orderBy("Sales").show()
# Descending call off the column itself.
df.orderBy(df["Sales"].desc()).show()
