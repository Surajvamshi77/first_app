import streamlit as st
import os
from matplotlib import image
st.title(' :red[INNOMATICS]')
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "JOBPORTAL-1638883616.jpeg")
img = image.imread(IMAGE_PATH)
st.image(img)
st.text('please check the following')
if st.button('LINK'):
    st.write('https://www.innomatics.in/')
    st.snow()
elif st.button('INSTAGRAM'):
    st.write('https://www.instagram.com/innomatics_hyd/?hl=en')
    st.balloon()
elif st.button('LINKEDIN'):
    st.write('https://www.linkedin.com/school/innomatics-research-labs/?originalSubdomain=in')
else:
    st.write('https://www.fb.com')
