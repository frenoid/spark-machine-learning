# Titanic logistic regression
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Titanic logistic regression').getOrCreate()
# Load dataset
data = spark.read.csv('titanic.csv',inferSchema=True,header=True)

data.printSchema()
data.columns

# Use numeric columns
my_cols = data.select(['Survived',
'Pclass',
'Sex',
'Age',
'SibSp',
'Parch',
'Fare',
'Embarked'])
# drop missing data
my_final_data = my_cols.na.drop()
# working with categorical columns
from pyspark.ml.feature import (VectorAssembler,VectorIndexer,OneHotEncoder,StringIndexer)
# Assign number to each of category, e.g: male female -> 0 1
gender_indexer = StringIndexer(inputCol='Sex',outputCol='SexIndex')
# One hot encoder: male ->[1, 0], female -> [0,1], each category will be converted into vector
gender_encoder = OneHotEncoder(inputCol='SexIndex',outputCol='SexVec')
embark_indexer = StringIndexer(inputCol='Embarked',outputCol='EmbarkIndex')
embark_encoder = OneHotEncoder(inputCol='EmbarkIndex',outputCol='EmbarkVec')
# assemble all into features
assembler = VectorAssembler(inputCols=['Pclass',
'SexVec',
'Age',
'SibSp',
'Parch',
'Fare',
'EmbarkVec'], outputCol='features')
from pyspark.ml.classification import LogisticRegression
# Pipeline, create stages for different steps
from pyspark.ml import Pipeline
log_reg_titantic = LogisticRegression(featuresCol='features', labelCol='Survived')
# create pipeline
pipeline = Pipeline(stages=[gender_indexer,
                    embark_indexer,
                    gender_encoder,
                    embark_encoder,
                    assembler,
                    log_reg_titantic])
train_titanic_data, test_titanic_data = my_final_data.randomSplit([0.7,0.3])
# fit model
fit_model = pipeline.fit(train_titanic_data)
# test model using test data
results = fit_model.transform(test_titanic_data)
# evaluate model
from pyspark.ml.evaluation import BinaryClassificationEvaluator
my_eval = BinaryClassificationEvaluator(rawPredictionCol='prediction',labelCol='Survived')
results.select('Survived','prediction').show()
AUC = my_eval.evaluate(results)
print("AUC is: "+ str(AUC))
