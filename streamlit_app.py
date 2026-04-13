import streamlit as st
import pandas as pd

st.title('Your Personal Japan Itinerary')
st.divider()
st.write('*Select your traveling preferences*')

type = st.multiselect("What kind of places do you prefer?", ["Urban", "Culture", "Nature", "Amusement Park"])
st.caption("_'Culture'_ includes castle, shrine, temple, and historical museum")

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
month = st.segmented_control("What month will you probably visit Japan?", months, selection_mode="multi")

SeasonTable = [['Month:','Mar - May','Jun - Aug','Sep - Early Dec','Dec - Feb'],['Season:','spring','summer','autumn','winter']]
with st.expander("*See seasons and timing guide*"):
  st.table(SeasonTable, width="content")
  st.write('''**Important times (exact times depend on location)** \n
  Cherry blossom: late March - late April \n
  Rainy season: Mid May - Mid July \n
  Monsoon season: September \n
  Autumn/fall foliage: Late Oct - Early Dec \n
  ''')

RC1, RC2 = st.columns(2)
with RC1:
  region = st.multiselect("Do you have regions that you want to visit?", ["Hokkaido Island", "Tohoku (East Japan)", "Kanto (Greater Tokyo)", "Tokai / South Chubu (South of Central Japan)", "Hokuriku / North Chubu (North of Central Japan)", "Kansai (Greater Osaka-Kyoto)", "Chugoku (West Japan)", "Shikoku Island", "Kyushu Island"])
with RC2:
  with st.expander('*see regions map*'):
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Regions_and_Prefectures_of_Japan.svg/3840px-Regions_and_Prefectures_of_Japan.svg.png')