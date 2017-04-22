
# coding: utf-8

# In[20]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[68]:

ndata=pd.read_csv('new_dstrIPC_1_2014.csv')
del ndata["Unnamed: 0"]
del ndata["Unnamed: 0.1"]
ndata = ndata[pd.notnull(ndata["lat"])]
ndata = ndata[pd.notnull(ndata["long"])]
ndata=ndata[ndata["District"]!="Total"]
ndata.head(25)


# In[13]:

ndata.pivot_table(values=['Murder'],index=["States/UTs"],aggfunc=np.sum)


# In[69]:


mydata=ndata.groupby(['States/UTs'])['Murder','Rape'].sum()
mydata.plot(kind='bar',stacked=True)


# In[155]:

mydata=ndata.groupby(['States/UTs'])["lat","long","Rape"].mean()
mydata


# In[156]:

from mpl_toolkits.basemap import Basemap
m=Basemap(projection='mill',llcrnrlat=mydata.lat.min()-2,urcrnrlat=mydata.lat.max()+2,llcrnrlon=mydata.long.min()-2,urcrnrlon=mydata.long.max()+2,resolution='c',epsg=4269)
x,y=m(tuple(mydata.long),tuple(mydata.lat))


# In[158]:

for i in range(36):
    mydata.Rape[i]=mydata.Rape[i]/(mydata.Rape.max())


# In[159]:

plt.figure(figsize=(20,10))
m.arcgisimage(service="NatGeo_World_Map", verbose=True)
for i in range(len(x)):
    m.plot(x[i],y[i],'ro',markersize=20, alpha=mydata.Rape[i] )


# In[116]:

m1=Basemap(projection='mill',llcrnrlat=ndata.Dislat.min()-2,urcrnrlat=ndata.Dislat.max()+2,llcrnrlon=ndata.Dislong.min()-2,urcrnrlon=ndata.Dislong.max()+2,resolution='c',epsg=4269)
x,y=m(tuple(ndata.Dislong),tuple(ndata.Dislat))


# In[117]:

plt.figure(figsize=(20,10))
m.arcgisimage(service="NatGeo_World_Map", verbose=True)
m.plot(x,y,'ro',markersize=5, alpha=0.3 )


# In[121]:

color = np.random.rand(ndata["States/UTs"].unique().shape[0], 3)
plt.figure(figsize=(20,10))
m1=Basemap(projection='mill',llcrnrlat=mydata.lat.min()-2,urcrnrlat=mydata.lat.max()+2,llcrnrlon=mydata.long.min()-2,urcrnrlon=mydata.long.max()+2,resolution='c',epsg=4269)
m1.arcgisimage(service="NatGeo_World_Map", verbose=True)
c = 0
for i in ndata["States/UTs"].unique():
    x1, y1 = m(tuple(ndata.Dislong[(ndata["States/UTs"] == i)]), 
         tuple(ndata.Dislat[(ndata["States/UTs"] == i)]))
    m1.plot(x1,y1,'ro',markersize=5,alpha=0.9, color = color[c] )
    c += 1


# In[149]:

mydata1=ndata.groupby(['States/UTs'])['Murder','Rape','Kidnapping & Abduction_Total','Attempt to commit Rape','Dacoity'].sum()


# In[160]:

mydata1.transpose().loc[:,["Uttar Pradesh","Bihar","Goa"]].plot(kind='pie',subplots=True)


# In[ ]:




# In[ ]:



