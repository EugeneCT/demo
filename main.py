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


master_w_rain=pd.read_csv("master_w_rain_and_cluster.csv")
master=copy.deepcopy(master_w_rain)
lean=master[['distance','fare_amount','fare/km','passenger_count','cluster','pickup_hour','pickup_weekday','pickup_year', 'pickup_month', 'pickup_day','precip']]
# coor_df=master_w_rain[['pickup_longitude',
#        'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']]

st.write("Welcome")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")
# fig, ax = plt.subplots(2,1)
# fig.set_size_inches(30,30)
# sns.heatmap(lean.corr(),vmin = -1, vmax = +1,annot = True, cmap = 'coolwarm',ax=ax[0])
# sns.heatmap(lean.cov(),vmin = -1, vmax = +1,annot = True, cmap = 'coolwarm',ax=ax[1])

# st.write(fig)

""" Plotly map """
# color_scale = [(0, 'orange'), (1,'red')]
# fig = px.scatter_mapbox(master_w_rain, 
#                         lat="pickup_latitude", 
#                         lon="pickup_longitude", 
#                         hover_name="fare_amount", 
#                         hover_data=["pickup_hour", "pickup_day"],
#                         color="fare_amount",
#                         color_continuous_scale=color_scale,
#                         size="fare_amount",
#                         zoom=8, 
#                         height=1200,
#                         width=1200)

# fig.update_layout(mapbox_style="open-street-map")
# fig.show()
# st.plotly_chart( fig )

