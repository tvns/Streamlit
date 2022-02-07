import streamlit as st 


# Text input
#.................................................................................................................


txt_input = st.text_input('Enter your name', max_chars = 50)

pswd = st.text_input('Enter your password', type='password')



# Text Area
#.................................................................................................................


msg = st.text_area('Give your feedback')

st.write(msg)



# Input Numbers
#.................................................................................................................


st.number_input('Enter your age', 5, 100, step=1)



# Input Dates
#.................................................................................................................


st.date_input('Enter your date of birth')



# Input Time
#.................................................................................................................


st.time_input('When is the next class?')