# import the streamlit library
import streamlit as st
from PIL import Image

image = Image.open('TSPSC.png')
st.image(image, caption='Sunrise by the mountains')
st.header("TSPSC Group 1 Results")
st.subheader("TSPSC Group 1 Results soon in december")
st.text("TSPSC RESULTS WILL BE SOON PUBLISHED in below Link {}".format("https://www.tspsc.gov.in/"))