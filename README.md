# spark-machine-learning

This is a demonstration of supervised and unsupervised machine learning techniques in Spark

The workshop was given as part of the [Big Data Engineering for Analytics](https://www.iss.nus.edu.sg/executive-education/course/detail/big-data-engineering-for--analytics/data-science) module which fulfills a requirement for the Engineering Big Data certificate issued by [NUS-ISS](https://www.iss.nus.edu.sg/)

This project translates the original workshop Pyspark code into Scala

## Data

The data was provided by [Dr LIU FAN from NUS-ISS](https://www.iss.nus.edu.sg/about-us/iss-team/teaching-staff/software-engineering-design)

Data source details TBA

## Structure
Each Scala object contains an example of a machine learning method
1. [Linear Regression on Sample Data](src/main/scala/com/normanlimxk/SparkML/LinearRegressionSample.scala)
2. [Linear Regression on Ecommerce Data](src/main/scala/com/normanlimxk/SparkML/LinearRegressionEcommerce.scala)


The project uses the [spark-sbt.g8 template from MrPowers](https://github.com/MrPowers/spark-sbt.g8)


