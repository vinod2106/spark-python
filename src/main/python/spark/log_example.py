from pyspark.conf import SparkConf
from pyspark.sql import SparkSession

myconf = SparkConf()
myconf.setMaster("local").setAppName("DB2_Test")
spark = SparkSession\
 .builder\
 .appName("Test")\
 .config(conf = myconf) \
 .getOrCreate()


Logger= spark._jvm.org.apache.log4j.Logger
mylogger = Logger.getLogger(__name__)
mylogger.error("some error trace")
mylogger.info("some info trace")
print("vinod")