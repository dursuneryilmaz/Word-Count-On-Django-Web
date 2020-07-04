from pyspark import SparkConf
from pyspark import SparkContext


def count(app_name, file):
    conf = SparkConf().setAppName(app_name)
    sc = SparkContext(conf=conf)

    rdd = sc.textFile(file)
    lines = rdd.count()

    words = rdd.flatMap(lambda line: line.split(" "))
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a+b)
    # wordCounts.saveAsTextFile("D:/WorkspaceSpark/output/")
    words = []

    for i in wordCounts.collect():
        words.append(i)

    sc.stop()
    return lines, words
