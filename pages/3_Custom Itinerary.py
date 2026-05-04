import streamlit as st
import pandas as pd

# Header
st.title('Custom Itinerary')
st.write('*Build your own itinerary from cities of your choice*')
st.divider()
dicti = {}


# Place
dicti['Culture'] = ['castle', 'Shinto shrine', 'Buddha temple', 'historical place']
dicti['Nature'] = ['mountains', 'river/gorge', 'lake', 'beach/coast', 'snow', 'Japanese garden', 'flower park']
dicti['Amusement Park'] = ['DisneyLand, Tokyo', 'DisneySea, Tokyo', 'Universal Studio, Osaka']
def TypeDetail (TDi):
    TDu = st.pills(TDi+' *(you can choose more than one)*:', dicti[TDi], selection_mode="multi")
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
  CB = st.segmented_control('Do you have the detailed times?', cb, selection_mode="multi")
  if 'Early-Mid Mar' in CB or 'Mid-Late May' in CB:
    st.caption('*sorry you cannot see cherry blossom in early-mid March or mid-late May*')

if 'Oct' in Month or 'Nov' in Month or 'Dec' in Month:
  st.write('You have a chance to see fall foliage in Japan!')
  ff = []
  for i in ['Oct','Nov','Dec']:
    if i in Month: ff += ['Early '+i,'Mid '+i,'Late '+i]
  FF = st.segmented_control('Do you have the detailed times?', ff, selection_mode="multi")
  if 'Late Dec' in FF:
    st.caption('*sorry you cannot see fall foliage in late December*')


# Duration
st.write('#####')
st.write('**How long will you stay in Japan?**')
Duration = st.slider('*Duration in days, including your arrival and departure day from Japan*', min_value=5, max_value=21)


# Region
st.write('#####')
RC1, RC2 = st.columns(2)
with RC1:
  st.write('**Do you have regions that you want to visit?**')
  regionU = st.multiselect("*you can choose more than one*", ["Hokkaido Island", "Tohoku (East Japan)", "Kanto (Greater Tokyo)", "Tokai / South Chubu (South of Central Japan)", "Hokuriku / North Chubu (North of Central Japan)", "Kansai (Greater Osaka-Kyoto)", "Chugoku (West Japan)", "Shikoku Island", "Kyushu Island"])
  st.caption('To make your visit efficient (time-wise and budget-wise), we recommend to explore no more than one region every 3-4 days of your visit. Choosing regions only adjacent to each other also helps make your visit more efficient!')
with RC2:
  with st.expander('*see regions map*'):
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Regions_and_Prefectures_of_Japan.svg/3840px-Regions_and_Prefectures_of_Japan.svg.png')

st.components.v1.iframe("https://www.google.com/maps/d/embed?mid=138-3NqgV3C79aEhKHId-sPNgskcHT70&ehbc=2E312F&noprof=1", height=600)


# Final
st.write('#####')
st.write('Ready to see your itineraries?')
filt = st.button('see itineraries', type='primary')

