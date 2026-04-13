import streamlit as st
import pandas as pd

st.title('Your Personal Japan Itinerary')
st.divider()
st.write('*Select your traveling preferences*')

type = st.multiselect("What kind of places do you prefer?", ["Urban", "Culture", "Nature", "Amusement Park"])
time = st.multiselect("When will you probably visit Japan?", ["Urban", "Culture", "Nature", "Amusement Park"])

