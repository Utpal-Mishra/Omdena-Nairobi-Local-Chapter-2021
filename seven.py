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
    
    st.header("LOCKDOWN PHASES")
    
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
    
    data = data.melt(id_vars=["Date"], var_name = "City", value_name = "Cases")
    data['Date'] = pd.to_datetime(data['Date'])
    data.sort_values(["Date", "City"], inplace = True)
    data = data[['City', 'Date', 'Cases']]
    
    def plot(city, y):
      fig = go.Figure()
      fig.add_trace(go.Scatter(x = data[data.City == city].Date, y = data[data.City == city].Cases, name = "Cases", mode = "lines", line=dict(color='blue')))
      fig.add_trace(go.Scatter(x = ['2020-02-10', '2020-07-15', '2020-11-20', '2021-02-01', '2021-04-15', '2021-07-27', '2021-11-01', '2022-01-5'], 
                               y = [int(y/2), int(y/2), int(y/2), int(y/2), int(y/2), int(y/2), int(y/2), int(y/2)], 
                               mode="text", name="Labels", 
                               text=["No Lockdown", "1st Lockdown", "No Lockdown", "2nd Lockdown", "No Lockdown", "3rd Lockdown", "No Lockdown", "4th Lockdown"], 
                               textposition="top center"))
      fig.update_xaxes(title_text = "Date", rangeslider_visible=True, showline=True, linewidth=2, linecolor='black', mirror=True)
      fig.update_yaxes(title_text = "Cases", showline=True, linewidth=2, linecolor='black', mirror=True)
      #fig.add_hline(y=max(data[data.City == city].Cases))
      fig.update_layout(height=700, width=1400, title_text="Cases in Africa from 2020-21 :: " + city,
                          shapes = [dict(type = "rect", y0 = -3, y1 = y+10, x0="2020-01-03", x1="2020-03-23", name = "No Lockdown", fillcolor = "green", opacity = 0.5),
                                    dict(type = "rect", y0 = -3, y1 = y+10, x0="2020-03-23", x1="2020-11-11", name = "1st Lockdown", fillcolor = "red", opacity = 0.5),
                                    dict(type = "rect", y0 = -3, y1 = y+10, x0="2020-11-11", x1="2020-12-01", name = "No Lockdown", fillcolor = "green", opacity = 0.5), 
                                    dict(type = "rect", y0 = -3, y1 = y+10, x0="2020-12-01", x1="2021-04-01", name = "2nd Lockdown", fillcolor = "red", opacity = 0.5),
                                    dict(type = "rect", y0 = -3, y1 = y+10, x0="2021-04-01", x1="2021-05-01", name = "No Lockdown", fillcolor = "green", opacity = 0.5),
                                    dict(type = "rect", y0 = -3, y1 = y+10, x0="2021-05-01", x1="2021-10-01", name = "3rd Lockdown", fillcolor = "red", opacity = 0.5),
                                    dict(type = "rect", y0 = -3, y1 = y+10, x0="2021-10-01", x1="2021-12-01", name = "No Lockdown", fillcolor = "green", opacity = 0.5),
                                    dict(type = "rect", y0 = -3, y1 = y+10, x0="2021-12-01", x1="2022-02-21", name = "4rd Lockdown", fillcolor = "red", opacity = 0.5)]) 
      fig.show()
      
    
       
    st.subheader("Visualize All Lockdown Phases")
    
    
    if st.checkbox('Plot Bomet') :
    	plot('Bomet', max(data[data.City == 'Bomet'].Cases))
    
    if st.checkbox('Plot Bungoma') :
    	plot('Bungoma', max(data[data.City == 'Bungoma'].Cases))
    
    if st.checkbox('Plot Busia') :
    	plot('Busia', max(data[data.City == 'Busia'].Cases))
    
    if st.checkbox('Plot Elgeyo Marakwet') :
    	plot('Elgeyo Marakwet', max(data[data.City == 'Elgeyo Marakwet'].Cases))
    
    if st.checkbox('Plot Embu') :
    	plot('Embu', max(data[data.City == 'Embu'].Cases))
    
    if st.checkbox('Plot Garissa') :
    	plot('Garissa', max(data[data.City == 'Garissa'].Cases))
    
    if st.checkbox('Plot HomaBay') :
    	plot('HomaBay', max(data[data.City == 'HomaBay'].Cases))
    
    if st.checkbox('Plot Isiolo') :
    	plot('Isiolo', max(data[data.City == 'Isiolo'].Cases))
    
    if st.checkbox('Plot Kajiado') :
    	plot('Kajiado', max(data[data.City == 'Kajiado'].Cases))
    
    if st.checkbox('Plot Kakamega') :
    	plot('Kakamega', max(data[data.City == 'Kakamega'].Cases))
    
    if st.checkbox('Plot Kericho') :
    	plot('Kericho', max(data[data.City == 'Kericho'].Cases))
    
    if st.checkbox('Plot Kiambu') :
    	plot('Kiambu', max(data[data.City == 'Kiambu'].Cases))
    
    if st.checkbox('Plot Kilifi') :
    	plot('Kilifi', max(data[data.City == 'Kilifi'].Cases))
    
    if st.checkbox('Plot Kirinyaga') :
    	plot('Kirinyaga', max(data[data.City == 'Kirinyaga'].Cases))
    
    if st.checkbox('Plot Kisii') :
    	plot('Kisii', max(data[data.City == 'Kisii'].Cases))
    
    if st.checkbox('Plot Kisumu') :
    	plot('Kisumu', max(data[data.City == 'Kisumu'].Cases))
    
    if st.checkbox('Plot Kitui') :
    	plot('Kitui', max(data[data.City == 'Kitui'].Cases))
    
    if st.checkbox('Plot Kwale') :
    	plot('Kwale', max(data[data.City == 'Kwale'].Cases))
    
    if st.checkbox('Plot Laikipia') :
    	plot('Laikipia', max(data[data.City == 'Laikipia'].Cases))
    
    if st.checkbox('Plot Lamu') :
    	plot('Lamu', max(data[data.City == 'Lamu'].Cases))
    
    if st.checkbox('Plot Machakos') :
    	plot('Machakos', max(data[data.City == 'Machakos'].Cases))
    
    if st.checkbox('Plot Makueni') :
    	plot('Makueni', max(data[data.City == 'Makueni'].Cases))
    
    if st.checkbox('Plot Mandera') :
    	plot('Mandera', max(data[data.City == 'Mandera'].Cases))
    
    if st.checkbox('Plot Marsabit') :
    	plot('Marsabit', max(data[data.City == 'Marsabit'].Cases))
    
    if st.checkbox('Plot Meru') :
    	plot('Meru', max(data[data.City == 'Meru'].Cases))
    
    if st.checkbox('Plot Migori') :
    	plot('Migori', max(data[data.City == 'Migori'].Cases))
    
    if st.checkbox('Plot Mombasa') :
    	plot('Mombasa', max(data[data.City == 'Mombasa'].Cases))
    
    if st.checkbox('Plot Muranga') :
    	plot('Muranga', max(data[data.City == 'Muranga'].Cases))
    
    if st.checkbox('Plot Nairobi') :
    	plot('Nairobi', max(data[data.City == 'Nairobi'].Cases))
    
    if st.checkbox('Plot Nakuru') :
    	plot('Nakuru', max(data[data.City == 'Nakuru'].Cases))
    
    if st.checkbox('Plot Nandi') :
    	plot('Nandi', max(data[data.City == 'Nandi'].Cases))
    
    if st.checkbox('Plot Narok') :
    	plot('Narok', max(data[data.City == 'Narok'].Cases))
    
    if st.checkbox('Plot Nyamira') :
    	plot('Nyamira', max(data[data.City == 'Nyamira'].Cases))
    
    if st.checkbox('Plot Nyandarua') :
    	plot('Nyandarua', max(data[data.City == 'Nyandarua'].Cases))
    
    if st.checkbox('Plot Nyeri') :
    	plot('Nyeri', max(data[data.City == 'Nyeri'].Cases))
    
    if st.checkbox('Plot Samburu') :
    	plot('Samburu', max(data[data.City == 'Samburu'].Cases))
    
    if st.checkbox('Plot Siaya') :
    	plot('Siaya', max(data[data.City == 'Siaya'].Cases))
    
    if st.checkbox('Plot TaitaTaveta') :
    	plot('TaitaTaveta', max(data[data.City == 'TaitaTaveta'].Cases))
    
    if st.checkbox('Plot TanaRiver') :
    	plot('TanaRiver', max(data[data.City == 'TanaRiver'].Cases))
    
    if st.checkbox('Plot Tharaka Nithi') :
    	plot('Tharaka Nithi', max(data[data.City == 'Tharaka Nithi'].Cases))
    
    if st.checkbox('Plot Trans Nzoia') :
    	plot('Trans Nzoia', max(data[data.City == 'Trans Nzoia'].Cases))
    
    if st.checkbox('Plot Turkana') :
    	plot('Turkana', max(data[data.City == 'Turkana'].Cases))
    
    if st.checkbox('Plot Uasin Gishu') :
    	plot('Uasin Gishu', max(data[data.City == 'Uasin Gishu'].Cases))
    
    if st.checkbox('Plot Vihiga') :
    	plot('Vihiga', max(data[data.City == 'Vihiga'].Cases))
    
    if st.checkbox('Plot Wajir') :
    	plot('Wajir', max(data[data.City == 'Wajir'].Cases))
    
    if st.checkbox('Plot West Pokot') :
    	plot('West Pokot', max(data[data.City == 'West Pokot'].Cases))
            
            
            
    ########################################################################### 