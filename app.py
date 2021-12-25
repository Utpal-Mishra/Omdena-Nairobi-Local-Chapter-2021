import home
import one 
import two
import three
import status

import streamlit as st

st.audio(open('inspire.mp3', 'rb').read(), format='audio/ogg')

PAGES = {
    "Home": home,
    "COVID-19 Data Analysis": one,
    "Lockdown Phases": two,
    "Cases & Fatalities": three,
    "Find Weather Status": status
}

st.sidebar.title('Navigation Bar')

selection = st.sidebar.selectbox("Go to: \n", list(PAGES.keys()))
page = PAGES[selection]
page.app()