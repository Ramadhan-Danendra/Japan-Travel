import streamlit as st
import pandas as pd


# Header
st.title('Preset Itinerary')
st.write('*Find your personalized itinerary among our curated itineraries*')
st.divider()
dicti = {}


# Place
dicti['Amusement Park'] = ['DisneyLand, Tokyo', 'DisneySea, Tokyo', 'Universal Studio, Osaka']
def TypeDetail (TDi):
    TDu = st.pills(TDi+' *(you can choose more than one)*:', dicti[TDi], selection_mode="multi")
    return(TDu)

st.write('**What kind of places do you want to visit?**')
Type = st.pills('*you can choose more than one*', ['Urban', 'Culture', 'Nature', 'Amusement Park'], selection_mode="multi")
st.caption("_'Culture'_ includes castle, shrine, temple, history museum, and other historical places")

if 'Amusement Park' in Type:
  TD = TypeDetail('Amusement Park')


# Time
st.write('#####')
st.write('**What month will you probably visit Japan?**')
month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
Month = st.segmented_control('*you can choose more than one*', month, selection_mode="multi")

SeasonTable = [['Month:','Mar - May','Jun - Aug','Sep - Early Dec','Dec - Feb'],['Season:','spring','summer','autumn','winter']]
with st.expander("*see season and timing guide*"):
  st.table(SeasonTable, width="content")
  st.write('''**Important times (exact times depend on location):** \n
  Cherry blossom: late March - late April \n
  Rainy season: Mid May - Mid July \n
  Monsoon season: September \n
  Autumn/fall foliage: Late Oct - Early Dec \n
  ''')

if 'Mar' in Month or 'Apr' in Month or 'May' in Month:
  st.write('You have a chance to see cherry blossom in Japan!')
  cb = []
  if 'Mar' in Month: cb += ['Early-Mid Mar','Late Mar']
  if 'Apr' in Month: cb += ['Early Apr','Mid Apr','Late Apr']
  if 'May' in Month: cb += ['Early May','Mid-Late May']
  CB = st.segmented_control('Do you have the detailed times? Ignore this if you aren't interested in cherry blossom', cb, selection_mode="multi")
  st.caption('Note: cherry blossom time can change every year. The data in this website are based on 2026 cherry blossom time from Japan Meteorological Corporation')
  if 'Early-Mid Mar' in CB or 'Mid-Late May' in CB:
    st.caption('*sorry you cannot see cherry blossom in early-mid March or mid-late May*')

if 'Oct' in Month or 'Nov' in Month or 'Dec' in Month:
  st.write('You have a chance to see fall foliage in Japan!')
  ff = []
  for i in ['Oct','Nov','Dec']:
    if i in Month: ff += ['Early '+i,'Mid '+i,'Late '+i]
  FF = st.segmented_control('Do you have the detailed times? Ignore this if you aren't interested in fall foliage', ff, selection_mode="multi")
  st.caption('Note: fall foliage time can change every year. The data in this website are based on average fall foliage time from Japan Meteorological Corporation')
  if 'Late Dec' in FF:
    st.caption('*sorry you cannot see fall foliage in late December*')


# Duration
st.write('#####')
st.write('**How long will you stay in Japan?**')
Duration = st.segmented_control('*This includes your arrival and departure day*', ['7 days', '10 days', '14 days'])
st.write('Want to set custom duration? Check the custom itinerary or the automatically generated itinerary')
 

# Region
st.write('#####')
RC1, RC2 = st.columns(2)
with RC1:
  st.write('**Do you have regions that you want to visit?**')
  Region = st.multiselect("*you can choose more than one*", ["Hokkaido Island", "Tohoku (East Japan)", "Kanto (Greater Tokyo)", "Tokai / South Chubu (South of Central Japan)", "Hokuriku / North Chubu (North of Central Japan)", "Kansai (Greater Osaka-Kyoto)", "Chugoku (West Japan)", "Shikoku Island", "Kyushu Island"])
with RC2:
  with st.expander('*see regions map*'):
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Regions_and_Prefectures_of_Japan.svg/3840px-Regions_and_Prefectures_of_Japan.svg.png')


# Difficulty
st.write('#####')
st.write('**Difficulty**')
Difficulty = st.segmented_control('*your maximum difficulty tolerance*', ['Very easy', 'Easy', 'Medium', 'Hard'])
with st.container(border=True):
  st.caption('''Very easy (recommended for first timer): stick to the super touristy Japan Golden Route (Tokyo, Kyoto, and Osaka) \n
  Easy: just hop off at the station and start exploring! \n
  Medium: require a little timing and schedule planning \n
  Hard: rare/no public transport, long transport duration''')


# Additional option
st.write('#####')
tokyoU = st.toggle('Include Tokyo in itinerary', value=True)

# Final
st.write('#####')
st.write('Ready to see your itineraries?')
filt = st.button('see itineraries', type='primary')