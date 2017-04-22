
# coding: utf-8

# In[15]:

import pandas as pd
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
tab=pd.read_csv("C:/Users/mohinder/Downloads/dstrIPC_1_2014.csv",index_col)
tab=tab[tab["District"]!="Total"]

g1=tab.groupby(["States/UTs"],as_index=False)[tab.columns.values].sum()
g1





# In[26]:

df = pd.read_csv("C:/Users/mohinder/Downloads/polStr_2013.csv")
# df
col = df.columns.values
col[0]="States/UTs"
col
df.columns=col
df
# df=df[df["DG/ADG"]<=100]


# In[27]:

get_ipython().magic('matplotlib inline')
import matplotlib.pylab
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
df.loc[:,"TOTAL"].plot(kind="bar" ,figsize=(10,10))


# In[37]:

newmerge = pd.merge(g1,df,on="States/UTs",how="left",sort=False)
n=newmerge.set_index('States/UTs')
n.loc[:,["Total Cognizable IPC crimes","TOTAL"]].plot(kind="bar" ,figsize=(10,10))
plt.title("Crime Rate Vs Police Force")

