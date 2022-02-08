from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator,MulticlassClassificationEvaluator

spark = SparkSession.builder.appName("logregdoc").getOrCreate()
# Load training data
data_set = spark.read.format("libsvm").option("numFeatures","692").load("sample_libsvm_data.txt")
data_set.show()
# Split into training set and testing set
lr_train, lr_test = data_set.randomSplit([0.7,0.3])
# Create LogisticRegression model
lgr_model = LogisticRegression()
# fit model with training set
fitted_model = lgr_model.fit(lr_train)
# evaluate with testing set
prediction_and_labels = fitted_model.evaluate(lr_test)
prediction_and_labels.predictions.show()
prediction_and_labels.predictions.select("probability").show(10, False)

my_eval = BinaryClassificationEvaluator()
final_roc = my_eval.evaluate(prediction_and_labels.predictions)
print(final_roc)