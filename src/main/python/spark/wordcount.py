from operator import add

from pyspark.sql import SparkSession

class WordCount:

    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

    inputFile = "../../resources/spark_notes.txt"
    lines = spark.read.text(inputFile).rdd.map(lambda r: r[0])
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))

    spark.stop()
    
if __name__ == "__main__":
    pass