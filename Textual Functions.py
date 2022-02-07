import streamlit as st
import pandas as pd 


# Textual Functions
#...................


st.text('This is a Text')



# String Formatting
#...................

name = 'TVNS Karthik'

st.text('My name is {}' .format('Karthik'))

st.text('My full name is {}' .format(name))



# Header
#........

st.header('This is a Header')

st.subheader('This is a SubHeader')



# Title
#.......

st.title('This is a Title')



# Markdown
#..........

st.markdown('# This is a Markdown text')

st.markdown('## This is a Markdown text')



# Bootstrap Text or Colorful Text
#.................................

st.success('Success')

st.warning('This is a warning')

st.info('Get a small suggestion')

st.error('This is an error')



# The superior write function
#.............................

st.write('This is a Text')

st.write('## This is a Markdown text')

st.write(12+9)

st.write(pd.DataFrame({'Name': ['Karthik'], 'Age': [25]}))

