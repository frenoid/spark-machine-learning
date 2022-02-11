# spark-machine-learning

This is a demonstration of supervised and unsupervised machine learning techniques in Spark

The workshop was given as part of the [Big Data Engineering for Analytics](https://www.iss.nus.edu.sg/executive-education/course/detail/big-data-engineering-for--analytics/data-science) module which fulfills a requirement for the Engineering Big Data certificate issued by [NUS-ISS](https://www.iss.nus.edu.sg/)

This project translates the original workshop Pyspark code into Scala

## Data

The data was provided by [Dr LIU FAN from NUS-ISS](https://www.iss.nus.edu.sg/about-us/iss-team/teaching-staff/software-engineering-design)
1. [Titanic dataset](https://kaggle.com/c/titanic/data)
2. [Seeds dataset](https://archive.ics.uci.edu/ml/datasets/seeds)


## Structure
Each class under src.main.scala.com.normanlimxk.SparkML contains examples of each Machine Learning method
1. [Linear Regression](src/main/scala/com/normanlimxk/SparkML/LinearRegression)
2. [Classification](src/main/scala/com/normanlimxk/SparkML/Classification)
3. [Clustering](src/main/scala/com/normanlimxk/SparkML/Clustering)

The project uses the [spark-sbt.g8 template from MrPowers](https://github.com/MrPowers/spark-sbt.g8)


