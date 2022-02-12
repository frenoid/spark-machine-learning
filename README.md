# spark-machine-learning

This is a demonstration of supervised and unsupervised machine learning techniques in Spark

This is **Workshop 11 Spark Machine Learning**  which one of a workshop series given as part of
the [Big Data Engineering for Analytics](https://www.iss.nus.edu.sg/executive-education/course/detail/big-data-engineering-for--analytics/data-science) module which fulfills a requirement for the Engineering Big Data certificate issued by [NUS-ISS](https://www.iss.nus.edu.sg/)

I have translated the original Python code to Scala

## Getting started

### Clone the repo
```
git clone https://github.com/frenoid/tour-of-spark.git
```
### Structure
1. [src/main/scala/com/normanlimxk/sparkworkshop](src/main/scala/com/normanlimxk/sparkworkshop) contains the Main Scala class
2. [src/main/resources](src/main/resources) contains data
3. [build.sbt](./build.sbt) contains a list of dependencies. Similar to pom.xml in Maven

### Running the Spark job
You have 2 options to run the spark job
1. Compile and run on a spark-cluster
2. Use Intellij (Recommended)

### (Option 1) Compile and run on a spark-cluster
Do this if you have a spark cluster to spark-submit to <br />
Take note of these versions. See also [build.sbt](./build.sbt)
```
scala = 2.12.10
spark = 3.0.3
sbt = 1.6.1
```
Use [sbt]((https://www.scala-sbt.org/)) to compile into a jar
```
sbt compile
```
The jar file will be in target/scala-2.12

Use spark-submit to submit the spark job
```
spark-submit {your-jar-file}
```

### (Option 2 RECOMMENDED) Use Intellij
Install [Intellij](https://www.jetbrains.com/idea/) and use it to Open the [build.sbt](./build.sbt) file as a Project

Intellij will resolve the dependencies listed in [build.sbt](./build.sbt)

Go to Run > Edit Configurations > Modify options > Add dependencies with "provided" scope to classpath

Run > Run class of your choice

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


