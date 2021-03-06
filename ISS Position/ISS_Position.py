#!/usr/bin/env python
# coding: utf-8

# Plots current location of the International Space Station

# Bring in libraries
import pandas as pd
import plotly.express as px

# Define static terms
url = 'http://api.open-notify.org/iss-now.json'
df = pd.read_json(url)

# Pull variables
df['latitude'] = df.loc['latitude','iss_position']
df['longitude'] = df.loc['longitude','iss_position']
df.reset_index(inplace=True)

# Remove unused variables
df = df.drop(['index','message'], axis=1)

# Setup map plot
fig = px.scatter_geo(df,lat='latitude',lon='longitude')

# Change symbol and show
fig.update_traces(marker=dict(size=25,symbol="star",color='red',opacity=0.5))
fig.show()
