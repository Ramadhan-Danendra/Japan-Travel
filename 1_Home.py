import streamlit as st
import pandas as pd

st.set_page_config(
  page_title = 'Japan Itinerary',
  page_icon = "🎴"
)

# Header
st.title('Your Personal Japan Itinerary')
st.divider()


st.page_link('pages/2_Preset Itinerary.py', label = 'Preset Itinerary', icon = ':material/alt_route﻿:')
st.caption('*find your personalized itinerary from our custom preset itinerary*')

st.page_link('pages/3_Custom Itinerary.py', label = 'Custom Itinerary', icon = ':material/conversion_path:')
st.caption('*build your own itinerary from cities of your choice*')

st.page_link('pages/4_Generated Itinerary.py', label = 'Generated Itinerary', icon = ':material/shape_line:')
st.caption('*Unhappy with our preset itineraries? Unfamiliar with Japan geography? Just select your traveling preferences and let the algorithm generates itinerary for you!*')
