import streamlit as st
import pandas as pd

# Header
st.title('Your Personal Japan Itinerary')
st.divider()
st.write('*Select your traveling preferences*')

# Place
st.write('What kind of places do you prefer?')
type = st.pills('*you can choose more than one*', ["Urban", "Culture", "Nature", "Amusement Park"], selection_mode="multi")
st.caption("_'Culture'_ includes castle, shrine, temple, history museum, and other historical places")

# Time
st.write(' ')
st.write('What month will you probably visit Japan?')
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
month = st.segmented_control('*you can choose more than one*', months, selection_mode="multi")

SeasonTable = [['Month:','Mar - May','Jun - Aug','Sep - Early Dec','Dec - Feb'],['Season:','spring','summer','autumn','winter']]
with st.expander("*see season and timing guide*"):
  st.table(SeasonTable, width="content")
  st.write('''**Important times (exact times depend on location):** \n
  Cherry blossom: late March - late April \n
  Rainy season: Mid May - Mid July \n
  Monsoon season: September \n
  Autumn/fall foliage: Late Oct - Early Dec \n
  ''')

# Region
st.write(' ')
RC1, RC2 = st.columns(2)
with RC1:
  st.write('Do you have regions that you want to visit?')
  region = st.multiselect("*you can choose more than one*", ["Hokkaido Island", "Tohoku (East Japan)", "Kanto (Greater Tokyo)", "Tokai / South Chubu (South of Central Japan)", "Hokuriku / North Chubu (North of Central Japan)", "Kansai (Greater Osaka-Kyoto)", "Chugoku (West Japan)", "Shikoku Island", "Kyushu Island"])
with RC2:
  with st.expander('*see regions map*'):
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Regions_and_Prefectures_of_Japan.svg/3840px-Regions_and_Prefectures_of_Japan.svg.png')

# Additional option
st.write(' ')
tokyo = st.toggle('Include Tokyo in itinerary', value=True)

# Final
st.write(' ')
st.write('Ready to see your itineraries?')
filt = st.button('see itineraries', type='primary')

