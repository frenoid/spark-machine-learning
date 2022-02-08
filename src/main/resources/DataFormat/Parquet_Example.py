from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName('ReadParquet').config("spark.driver.host","localhost").config("spark.ui.port","4040").getOrCreate()

peopleDF = spark.read.json("people.json")

# DataFrames can be saved as Parquet files, maintaining the schema information.
peopleDF.write.format("parquet").mode("overwrite").save("people.parquet")

# Read in the Parquet file created above.
# Parquet files are self-describing so the schema is preserved.
# The result of loading a parquet file is also a DataFrame.
parquetFile = spark.read.parquet("people.parquet")

# Parquet files can also be used to create a temporary view and then used in SQL statements.

parquetFile.createOrReplaceTempView("parquetFile")
teenagers = spark.sql("SELECT name FROM parquetFile WHERE age >= 13 AND age <= 19")
teenagers.show()

#spark.stop()
