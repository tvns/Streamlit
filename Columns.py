import streamlit as st 
from PIL import Image


# Web app Layout

img = Image.open('Web App Type.png')

st.image(img)

#........................................................................................................


st.write('### Billing Address')


country = ['India', 'Canada', 'USA', 'Germany', 'Australia']

st.selectbox('COUNTRY', country)



col1, col2 = st.columns(2)       # Because we need 2 columns

with col1:

	st.text_input('FIRST NAME')

with col2:

	st.text_input('LAST NAME')



st.text_area('ADDRESS')



city, state, zc = st.columns([4, 3, 2])       # Instead of putting no. of columns we are using the ratio to show the difference in size for each box

with city:

	st.text_input('CITY')

with state:

	st.text_input('STATE/PROVINCE')

with zc:

	st.text_input('ZIPCODE')



phone, mail = st.columns([2,3])

with phone:

	st.text_input('PHONE NUMBER')

with mail:

	st.text_input('EMAIL ADDRESS')



cancel, save = st.columns([1,7])

with cancel:

	if st.button('CANCEL'):

		st.error('Failed')

with save:

	if st.button('SAVE'):

		st.success('Submitted Succesfully')

	