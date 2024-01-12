import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import copy
import tqdm
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
from sklearn.preprocessing import LabelEncoder

master_w_rain=pd.read_csv("master_w_rain.csv")

# coor_df=master_w_rain[['pickup_longitude',
#        'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']]


st.write("Welcome")
color_scale = [(0, 'orange'), (1,'red')]

fig = px.scatter_mapbox(master_w_rain, 
                        lat="pickup_latitude", 
                        lon="pickup_longitude", 
                        hover_name="fare_amount", 
                        hover_data=["pickup_hour", "pickup_day"],
                        color="fare_amount",
                        color_continuous_scale=color_scale,
                        size="fare_amount",
                        zoom=8, 
                        height=1200,
                        width=1200)

fig.update_layout(mapbox_style="open-street-map")
# fig.show()
st.plotly_chart( fig )

