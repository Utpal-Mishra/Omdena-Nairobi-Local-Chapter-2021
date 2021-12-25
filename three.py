import streamlit as st
import time

import sys
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import plotly.express as px
from datetime import datetime as dt

from streamlit_metrics import metric, metric_row

sys.setrecursionlimit(100000)
#print("Installed Dependencies")


def app():
    st.title("COVID-19 BEFORE-DURING ANALYSIS IN NAIROBI")
    
    st.header("CASES BY AGE CATEGORIES")
    
    if st.checkbox('Plot Cases By Age Categories') :
    
        st.subheader("Loading the COVID-19 Data....")
        
        file = st.file_uploader("Upload file")
        show_file = st.empty()
        
        if not file:
            show_file.info("Please upload a file of type: " + ", ".join([".csv", ".xls", ".xlsx"]))
            return
        
        label = st.empty()
        bar = st.progress(0)
        
        for i in range(100):
            # Update progress bar with iterations
            label.text(f'Loaded {i+1} %')
            bar.progress(i+1)
            time.sleep(0.01)
        
        path = file #'new_master_data.csv'
        data = pd.read_csv(path)
        #print("Data Shape: ", data.shape)
        data.head()
        #print("Data Shape: ", data.shape)
        #data.head()
        
        ".... and now we're done!!!"
        
        ###########################################################################
        
        data = data.fillna(0)   
        data.isna().sum()
        data['Age_group'][1] = '10-19'
        
        data = data.melt(id_vars=["Age_group"], var_name = "Date", value_name = "Cases")
        data = data[['Date', 'Age_group', 'Cases']]
        data = data[data.Date != ' Science/data_pdfs/Press-Statement-on-Poland-Donation-September-13-2021']
        data.sort_values(["Date", 'Age_group'], inplace = True)
        
        def barplot(data):
          fig = px.bar(data, x=data.Age_group, y=data.Cases, animation_frame = data.Date, color=data.Age_group, barmode='group')
          fig.update_xaxes(title_text = "Age Categories", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'COVID-19 Cases', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=500, width=1400, title_text='Witnessed COVID-19 Cases For Different Age Groups') 
          
          st.plotly_chart(fig)
            
        barplot(data)
        
        data = data[['Age_group', 'Cases']].groupby('Age_group').sum()
        data = data.reset_index()
        fig = go.Figure(data=[go.Pie(labels=data.Age_group, values=data.Cases, hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='% of COVID-19 Cases For Different Age Groups') 
        st.plotly_chart(fig)
        
    ###########################################################################
    
    st.header("")
    st.header("")
    st.header("FATALITIES BY AGE CATEGORIES")
    
    if st.checkbox('Plot Fatalities By Age Categories') :
    
        st.subheader("Loading the COVID-19 Data....")
        
        file = st.file_uploader("Upload file")
        show_file = st.empty()
        
        if not file:
            show_file.info("Please upload a file of type: " + ", ".join([".csv", ".xls", ".xlsx"]))
            return
        
        label = st.empty()
        bar = st.progress(0)
        
        for i in range(100):
            # Update progress bar with iterations
            label.text(f'Loaded {i+1} %')
            bar.progress(i+1)
            time.sleep(0.01)
        
        path = file #'new_master_data.csv'
        data = pd.read_csv(path)
        #print("Data Shape: ", data.shape)
        data.head()
        #print("Data Shape: ", data.shape)
        #data.head()
        
        ".... and now we're done!!!"
        
        ###########################################################################
        
        data = data.fillna(0)   
        data.isna().sum()
        data['Age_Group'][1] = '10-19'
        
        data = data.melt(id_vars=["Age_Group"], var_name = "Date", value_name = "Cases")
        data = data[['Date', 'Age_Group', 'Cases']]
        data = data[data.Date != ' Science/data_pdfs/Press-Statement-on-Poland-Donation-September-13-2021']
        data.sort_values(["Date", 'Age_Group'], inplace = True)
        
        def barplot(data):
          fig = px.bar(data, x=data.Age_Group, y=data.Cases, animation_frame = data.Date, color=data.Age_Group, barmode='group')
          fig.update_xaxes(title_text = "Age Categories", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
          fig.update_yaxes(title_text = 'COVID-19 Fatalities', showline=True, linewidth=2, linecolor='black', mirror=True)
          # fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6)
          fig.update_layout(height=500, width=1400, title_text='Witnessed COVID-19 Fatalities For Different Age Groups') 
          st.plotly_chart(fig)
            
        barplot(data)
        
        data = data[['Age_Group', 'Cases']].groupby('Age_Group').sum()
        data = data.reset_index()
        fig = go.Figure(data=[go.Pie(labels=data.Age_Group, values=data.Cases, hole=.5)])
        fig.update_layout(height=500, width=1400, title_text='% of COVID-19 Fatalities For Different Age Groups') 
        st.plotly_chart(fig)
        