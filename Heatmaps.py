#!/usr/bin/env python
# coding: utf-8

# In[9]:


from urllib.request import urlopen
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
import seaborn
import matplotlib as mpl


# In[10]:


#load dataframe here (call it df)
#datafram contains date, county, and indoor activity metric
df = pd.read_csv("https://media.githubusercontent.com/media/bansallab/indoor_outdoor/main/indoor_activity_data/indoor_activity_2018_2020.csv?_sm_au_=iVV404tMNLPkLDTRpGsWvKttvN1NG")


# In[11]:


# Load geojson data with FIPS codes for county
#I think this is data for the county location/geographical data?
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
    
# Make sure county column is in the right format
# You might need to change the dataframe or column name here if your county column is not called 'county' or your dataframe is not called df
#changing data to the right type
#df.county = df.county.astype(float).astype(int).astype(str).str.zfill(5)


# In[12]:


df["date"] = pd.to_datetime(df["date"])


# In[15]:


df_montcounty = df.loc[df["county"] == 24031]
df_fredcounty = df.loc[df["county"] == 24021]
df_baltcounty = df.loc[df["county"] == 24510]


# In[16]:


df_montcounty


# In[17]:


seaborn.heatmap(data = df_montcounty)


# In[13]:


seaborn.heatmap(data = df)

