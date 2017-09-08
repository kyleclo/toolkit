import findspark
findspark.init()
from pyspark import SparkContext, SparkConf

import pandas as pd

df = pd.read_csv('...')
df_grouped = df.groupby(by=['id'])

x=1
y=2
z=3

lambda_map = lambda group_tuple: my_function(id=group_tuple[0], sub_df=group_tuple[1], x=x, y=y, z=z)

def spark_map(spark_context, iterable, map_function):
    results = spark_context.parallelize(iterable).map(map_function).collect()
    return results
    
sc = SparkContext(pyFiles=[ABS_PATH_TO_SOME_DEPENDENCY, ANOTHER_ONE])
results = spark_map(spark_context=sc,
                    iterable=df_grouped,
                    map_function=lambda_map)
sc.stop()

