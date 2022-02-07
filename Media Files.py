import streamlit as st 

from PIL import Image



# Image File
#.................................................................................................................


img = Image.open('messi.jpeg')

st.image(img)

st.image('https://p.imgci.com/db/PICTURES/CMS/293700/293795.jpg')




# Video File
#.................................................................................................................


vid = open('SampleVideo.mp4', 'rb')

st.video(vid)

st.video(vid, start_time = 15)




# Audio File
#.................................................................................................................


aud = open('SampleAudio.mp3', 'rb')

st.audio(aud)

st.audio(aud, start_time = 5)