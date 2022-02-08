from pyspark.sql import SparkSession
# Start SparkSession
spark = SparkSession.builder.appName("missingdata").getOrCreate()
df = spark.read.csv("ContainsNull.csv",header=True,inferSchema=True)
df.show()

# Drop any row that contains missing data
df.na.drop().show()
# Has to have at least 2 NON-null values
df.na.drop(thresh=2).show()
# Drop row “Sales” contains missing data
df.na.drop(subset=["Sales"]).show()
# Drop any row contains missing data
df.na.drop(how='any').show()
# Drop those rows contains missing data for all columns
df.na.drop(how='all').show()

# Fill missing data with “NEW VALUE”
df.na.fill('NEW VALUE').show()
# Fill missing data with 0
df.na.fill(0).show()
# Fill missing data in row “Name” with “No Name”
df.na.fill('No Name',subset=['Name']).show()
# Fill values with mean value for column “Sales”
import pyspark.sql.functions as F
mean_val = df.select(F.mean(df['Sales'])).collect()
# Weird nested formatting of Row object!
mean_val[0][0]
mean_sales = mean_val[0][0]
df.na.fill(mean_sales,["Sales"]).show()
