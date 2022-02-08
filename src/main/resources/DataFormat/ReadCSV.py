from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Read CSV files').getOrCreate()
from pyspark.sql.types import StructType, StructField, StringType,IntegerType

# Read CSV file people.csv
df = spark.read.format('csv') \
                .option("inferSchema","true") \
                .option("header","true") \
                .option("sep",";") \
                .load("people.csv")

# Show result
df.show()
# Print schema
df.printSchema()

# Define your own schema
schema = StructType([ \
    StructField("name",StringType(),True), \
    StructField("age",IntegerType(),True), \
    StructField("job",StringType(),True)])
peopleDF = spark.read.format('csv') \
                    .option("schema","shcema") \
                    .option("sep",";") \
                    .option("header","true") \
                    .load("people.csv")

#peopleDF = spark.read.load("people.csv", format = "csv", header = "true",sep=";",schema=schema)
peopleDF.show()
peopleDF.printSchema()