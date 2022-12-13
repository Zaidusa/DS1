# import the streamlit library
import streamlit as st
import os
ROOT_DIR = os.path.abspath(os.curdir)

print("root is",ROOT_DIR)

video_file = open('Bank.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)