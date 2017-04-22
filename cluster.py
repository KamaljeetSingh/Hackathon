
# coding: utf-8

# In[126]:

import pandas as pd
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
tab=pd.read_csv("C:/Users/lenovo/Downloads/dstrIPC_1_2014.csv")
tab=tab[tab["District"]!="Total"]
g1=tab.groupby(["States/UTs"],as_index=False)[tab.columns.values].sum()
g2 = g1.drop('States/UTs', 1)
g1



# In[160]:

from sklearn.cluster import KMeans

num_clusters = 3
km = KMeans(n_clusters=num_clusters)

get_ipython().magic('time km.fit(g2)')

clusters = km.labels_.tolist()
# print(clusters[1])
cluster_items={}
ss=g1["States/UTs"].tolist()

for i in range(0,36):
    cluster_items[clusters[i]].append(ss[i])
    

# for i,val in enumerate(clusters):
# #     print(i,val)
#     cluster_items[str(val)].append(g1.loc[i,"States/UTs"])



# In[144]:

g1.loc[1,"States/UTs"]


# In[156]:

g1["States/UTs"].tolist()


# In[155]:

len(clusters)


# In[171]:

d={"cluster":clusters,"state":g1["States/UTs"]}


# In[177]:

new=pd.DataFrame(d)
new[(new.cluster==0)]


# In[ ]:



