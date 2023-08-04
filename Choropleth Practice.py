#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


#load dataframe here (call it df)
#datafram contains date, county, and indoor activity metric
df = pd.read_csv("https://media.githubusercontent.com/media/bansallab/indoor_outdoor/main/indoor_activity_data/indoor_activity_2018_2020.csv?_sm_au_=iVV404tMNLPkLDTRpGsWvKttvN1NG")


# In[3]:


df


# In[4]:


# Load geojson data with FIPS codes for county
#I think this is data for the county location/geographical data?
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
    
# Make sure county column is in the right format
# You might need to change the dataframe or column name here if your county column is not called 'county' or your dataframe is not called df
#changing data to the right type
df.county = df.county.astype(float).astype(int).astype(str).str.zfill(5)


# In[5]:


df


# In[6]:


counties
#To choose for a specific date
df["date"] = pd.to_datetime(df["date"])
df_date_1 = df.loc[df["date"] == "2018-1-7"]
df_date_1

# In[6]:


#initializing choropleth. location, color, scope, colorscale
fig = px.choropleth(df,                 # name of your dataframe
                    geojson=counties,
                    locations='county', # name of column in df that has the county fips
                    color='indoor_activity',      # name of column in df that has the data you want to plot
                    color_continuous_scale= px.colors.diverging.Picnic, # can choose colorscale from https://plotly.com/python/builtin-colorscales/
                    scope='usa'
                   )


# In[7]:


##############################################
# All the code below will let you control the characterisitcs of the map
# I would ignore it for now and add it in later as needd
fig.update_layout(margin=dict(b=0, t=0, l=0, r=0),  # sets the margins of the plot w/in its div
                  # controls appearance of hover label
                  hoverlabel=dict(bgcolor='white', font_size=16),
                  # controls appearance of color bar & title
                  coloraxis_colorbar=dict(
                      lenmode='pixels', len=400,
                      thicknessmode='pixels', thickness=40,
                      ticks='outside',
                      title='Indoor Activity' # Change title here
                  ),
                  # modifications to the map appearance (special geo settings)
                  geo=dict(
                      showlakes=False,
                      showland=True, landcolor='white'
                  )
                  )
fig.update_coloraxes(colorbar_title_font=dict(size=14)) # set the fontsize of the colorbar title

fig.update_traces(marker_line_width=0.3,  # controls county border line width
                  marker_opacity=0.85,  # changes fill color opacity to let state borders through
                  marker_line_color='#262626',  # controls county border color; needs to be darker than "states"
                  )


# In[ ]:




