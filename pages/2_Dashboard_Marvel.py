import streamlit as st
import pandas as pd
from matplotlib import image
import os

st.title("Dashboard - Marvel Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
print(FILE_DIR)
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
print(PARENT_DIR)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "marvel-dc-dwayne-johnson.webp")
DATA_PATH = os.path.join(dir_of_interest, "data", "db.csv")

img = image.imread(IMAGE_PATH)
df = pd.read_csv(DATA_PATH,encoding = 'unicode_escape')
st.image(img)
st.dataframe(df)