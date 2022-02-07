import streamlit as st 


# Buttons
#...................................................................................................................................

click = st.button('Submitted')

if click:

	st.success('Submitted succesffuly')




# If we give same name for multiple buttons it will throw an error
# Hence, we have to use key and give any value to the key
#....................................................................................................................................

press = st.button('Submitted', key = 'second')

if press:

	st.warning('File already submitted')




# Radio Buttons
#....................................................................................................................................



touch = st.radio('What is the Review of the movie?', ('Good', 'Average', 'Bad'))


if touch == 'Good':

	st.text('Good to hear that')


elif touch == 'Average':

	st.text('Thanks for watching the movie')


else:

	st.text('Will improve next time')





# Checkbox
#...................................................................................................................................


if st.checkbox('Show/Hide'):

	st.warning('This is a confidential information')





# Expander
#...................................................................................................................................


with st.expander('Show me the password'):

	st.warning('Keep it confidential')





# Selection
#...................................................................................................................................


lang = ['Python', 'R', 'Java', 'C++']

selected = st.selectbox('Select the language for IDE', lang)

st.write('Selected language is {}'.format(selected))


languages_selected = st.multiselect('Select your favourite languages', lang, default='Python')

st.write('Selected languages are {}' .format(languages_selected))





# Slider
#...................................................................................................................................


Age = st.slider('Enter your age:', 1, 100, 20, step = 2)


band = ['Violet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']

Colour = st.select_slider('Select the color', options = band)













