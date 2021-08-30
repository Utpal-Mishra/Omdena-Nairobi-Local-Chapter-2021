import home
import one 
import two
import three
import four
import five
import eight
import seven
import status

import streamlit as st

st.audio(open('inspire.mp3', 'rb').read(), format='audio/ogg')

PAGES = {
    "Home": home,
    "COVID-19 Data Analysis": one,
    "No Lockdown Phase": two,
    "1st Lockdown Phase": three,
    "2nd Lockdown Phase": four,
    "3rd Lockdown Phase": five,
    "Compare Lockdown Phases": eight,
    "Region-Wise Analysis": seven,
    "Find Weather Status": status
}

st.sidebar.title('Navigation Bar')

selection = st.sidebar.selectbox("Go to: \n", list(PAGES.keys()))
page = PAGES[selection]
page.app()