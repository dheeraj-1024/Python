# Basics of Pandas DataFrames

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
iris =  pd.read_csv(csv_url, names = col_names)
# general stats about data
iris.describe()
# box-whisker plot
iris.boxplot()
# datatypes
iris.dtypes
# To check null values
iris.info()

# Making Dataframe
x=np.array([["one","one","one","two","two","two"],["A","B","C","A","B","C"],[i for i in range(1,7)],["x","y","z","a","b","c"]])
x=x.transpose()
# Converting array to DataFrame
df=pd.DataFrame(x,index=[i for i in range(3,9)],columns=["foo","bar","baz","zoo"])
# Making pivot table
df.pivot(index="foo",columns="bar",values="baz")
# Adding new columns to df
df["Added_Row"]=[i for i in range(20,26)]
