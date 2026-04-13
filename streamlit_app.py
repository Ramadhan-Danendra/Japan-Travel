import streamlit as st
import pandas as pd

st.title('Your Personal Japan Itinerary')
st.divider()
st.write('*Select your traveling preferences*')

st.write('What kind of places do you prefer?')
urban = st.checkbox("Urban")
culture = st.checkbox("Culture")
nature = st.checkbox("Nature")
st.write(urban, culture, nature)

st.write('What season will you probably visit Japan?')
spring = st.checkbox("Spring")
summer = st.checkbox("Summer")
autumn = st.checkbox("Autumn")
winter = st.checkbox("Winter")


A = [spring,summer,autumn,winter]
for i in A:
    st.write(i);

type = st.multiselect(
    "What kind of places do you prefer?",
    ["Urban", "Culture", "Nature", "Park"])

st.write(type)
for i in type:
    st.write(i);