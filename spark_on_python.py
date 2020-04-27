from pyspark import SparkContext

sc = SparkContext(appName='test')

path = '/data/'

students = sc.textFile(path + 'students.txt')

students \
    .map(lambda line: (line.split(",")[4], 1)) \
    .reduceByKey(lambda a, b: a + b) \
    .map(lambda a: str(str(a[0]).encode('utf-8'))+str(a[1])) \
    .saveAsTextFile(path + 'out')
