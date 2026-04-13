import streamlit as st
import pandas as pd

st.title('Your Personal Japan Itinerary')
st.divider()
st.write('*Select your traveling preferences*')

type = st.multiselect("What kind of places do you prefer?", ["Urban", "Culture", "Nature", "Amusement Park"])
st.caption("_'Culture'_ includes castle, shrine, temple, and historical museum")

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
month = st.segmented_control("What month will you probably visit Japan?", months, selection_mode="multi")
SeasonTable = [['Mar - May','Jun - Aug','Sep - Early Dec','Dec - Feb'],['spring','summer','autumn','winter']]
st.table(SeasonTable, width="content")
st.write('''Important times (exact times depend on location) \n
Cherry blossom: late March - late April \n
Rainy season: Mid May - Mid July \n
Monsoon season: September \n
Autumn/fall foliage: Late Oct - Early Dec \n
''')

region = st.multiselect("Do you have regions that you want to visit?", ["Hokkaido Island", "Tohoku (East Japan)", "Kanto (Greater Tokyo)", "Tokai (South of Central Japan)", "Hokuriku (North of Central Japan)", "Kansai (Greater Osaka-Kyoto)", "Chugoku (West Japan)", "Shikoku Island", "Kyushu Island"])
