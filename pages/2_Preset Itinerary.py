import streamlit as st
import pandas as pd


# Header
st.title('Preset Itinerary')
st.write('*Find your personalized itinerary from our custom, preset itinerary*')
st.divider()
dicti = {}


# Place
dicti['Culture'] = ['castle', 'Shinto shrine', 'Buddha temple', 'historical place']
dicti['Nature'] = ['mountains', 'river/gorge', 'lake', 'snow', 'Japanese garden', 'flower park']
dicti['Amusement Park'] = ['DisneyLand, Tokyo', 'DisneySea, Tokyo', 'Universal Studio, Osaka']
def TypeDetail (TDi):
    TDu = st.pills(TDi+': *(you can choose more than one)*', dicti[TDi], selection_mode="multi")
    return(TDu)

st.write('**What kind of places do you want to visit?**')
Type = st.pills('*you can choose more than one*', ['Urban', 'Culture', 'Nature', 'Amusement Park'], selection_mode="multi")
st.caption("_'Culture'_ includes castle, shrine, temple, history museum, and other historical places")

TypeTD = Type
if 'Urban' in TypeTD: TypeTD.remove('Urban')
TD = []
for i in TypeTD:
    TD.extend(TypeDetail(i))


# Time
st.write('#####')
st.write('**What month will you probably visit Japan?**')
month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
monthU = st.segmented_control('*you can choose more than one*', month, selection_mode="multi")

SeasonTable = [['Month:','Mar - May','Jun - Aug','Sep - Early Dec','Dec - Feb'],['Season:','spring','summer','autumn','winter']]
with st.expander("*see season and timing guide*"):
  st.table(SeasonTable, width="content")
  st.write('''**Important times (exact times depend on location):** \n
  Cherry blossom: late March - late April \n
  Rainy season: Mid May - Mid July \n
  Monsoon season: September \n
  Autumn/fall foliage: Late Oct - Early Dec \n
  ''')

if 'Mar' in monthU or 'Apr' in monthU:
  st.write('You have a chance to see cherry blossom in Japan!')
  CB = []
  if 'Mar' in monthU: CB += ['Early-Mid Mar','Late Mar']
  if 'Apr' in monthU: CB += ['Early Apr','Mid Apr','Late Apr']
  cbU = st.segmented_control('Do you have the detailed times?', CB, selection_mode="multi")
  if 'Early-Mid Mar' in cbU:
    st.caption('*sorry you cannot see cherry blossom in early-mid March*')

if 'Oct' in monthU or 'Nov' in monthU or 'Dec' in monthU:
  st.write('You have a chance to see fall foliage in Japan!')
  FF = []
  for i in ['Oct','Nov','Dec']:
    if i in monthU: FF += ['Early '+i,'Mid '+i,'Late '+i]
  ffU = st.segmented_control('Do you have the detailed times?', FF, selection_mode="multi")
  if 'Late Dec' in ffU:
    st.caption('*sorry you cannot see fall foliage in late December*')
  

# Region
st.write('#####')
RC1, RC2 = st.columns(2)
with RC1:
  st.write('**Do you have regions that you want to visit?**')
  regionU = st.multiselect("*you can choose more than one*", ["Hokkaido Island", "Tohoku (East Japan)", "Kanto (Greater Tokyo)", "Tokai / South Chubu (South of Central Japan)", "Hokuriku / North Chubu (North of Central Japan)", "Kansai (Greater Osaka-Kyoto)", "Chugoku (West Japan)", "Shikoku Island", "Kyushu Island"])
with RC2:
  with st.expander('*see regions map*'):
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Regions_and_Prefectures_of_Japan.svg/3840px-Regions_and_Prefectures_of_Japan.svg.png')


# Duration
st.write('#####')
st.write('**How long will you stay in Japan?**')
Duration = st.segmented_control('This includes your arrival and departure day', ['7 days', '10 days', '14 days'])
st.write('Want to set custom duration? Check the custom itinerary or the automatically generated itinerary')


# Additional option
st.write('#####')
tokyoU = st.toggle('Include Tokyo in itinerary', value=True)

# Final
st.write('#####')
st.write('Ready to see your itineraries?')
filt = st.button('see itineraries', type='primary')