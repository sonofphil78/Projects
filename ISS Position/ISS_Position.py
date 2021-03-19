#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import plotly.express as px


# In[9]:


url = 'http://api.open-notify.org/iss-now.json'
df = pd.read_json(url)


# In[10]:


df


# In[11]:


df['latitude'] = df.loc['latitude','iss_position']
df['longitude'] = df.loc['longitude','iss_position']
df.reset_index(inplace=True)
df = df.drop(['index','message'], axis=1)


# In[12]:


df


# In[13]:


fig = px.scatter_geo(df,lat='latitude',lon='longitude')


# In[14]:


fig.show()


# In[ ]:





