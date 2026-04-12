import streamlit as st
import pandas as pd

st.title('Your Personal Japan Itinerary App')
st.write('*Select your traveling preferences*')

st.write('What kind of places do you prefer?')
urban = st.checkbox("Urban")
culture = st.checkbox("Culture")
nature = st.checkbox("Nature")

st.write(urban, culture, nature)
