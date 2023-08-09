#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go


# In[33]:


#load dataframe here (call it df)
#datafram contains date, county, and indoor activity metric
df = pd.read_csv("https://media.githubusercontent.com/media/bansallab/indoor_outdoor/main/indoor_activity_data/indoor_activity_2018_2020.csv?_sm_au_=iVV404tMNLPkLDTRpGsWvKttvN1NG")


# In[3]:


# Load geojson data with FIPS codes for county
#I think this is data for the county location/geographical data?
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
    
# Make sure county column is in the right format
# You might need to change the dataframe or column name here if your county column is not called 'county' or your dataframe is not called df
#changing data to the right type
#df.county = df.county.astype(float).astype(int).astype(str).str.zfill(5)


# In[34]:


df["date"] = pd.to_datetime(df["date"])


# In[5]:


northSouth = pd.read_csv("community_structure_feasible_2018_2019dec2022_final.csv")
northSouth


# In[7]:


northSouth.rename(columns = {'node':'county'}, inplace = True)
northSouth


# In[28]:


ns = northSouth.set_index('county').to_dict()['modularity_class']
ns


# In[35]:


df


# In[36]:


df["Modularity"] = ns
df


# In[39]:


df["Modularity"] = df["county"].map(ns)
df


# In[41]:


clusterA = df.loc[df["Modularity"] == 0.0]
clusterB = df.loc[df["Modularity"] == 1.0]


# In[42]:


clusterA


# In[44]:


clusterA.plot("date","indoor_activity", 
                   title = "Cluster A Seasonality Plot", xlabel = "Date", ylabel = "Indoor Ac")


# In[45]:


clusterB.plot("date","indoor_activity", 
                   title = "Cluster B Seasonality Plot", xlabel = "Date", ylabel = "Indoor Ac")

