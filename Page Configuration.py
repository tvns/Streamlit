import streamlit as st 
from PIL import Image


img = Image.open('messi.jpeg')

st.set_page_config(page_title = 'Page config', page_icon = img, layout = 'wide', initial_sidebar_state = 'expanded')



def main():

	st.header('Page configuration')

	st.sidebar.success('Menu')


main()