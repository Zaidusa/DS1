	# import the streamlit library
import pickle
from pathlib import Path

import streamlit as st
from PIL import Image
import os
ROOT_DIR = os.path.abspath(os.curdir)

st.title("CIBIL-The higher your score the better are your chances of getting a loan")

image = Image.open('Cibil-Score.jpg')
st.image(image, caption='Know your CIBIL- The higher your score the better are your chances of getting a loan')

# video_file = open('Bank.mp4', 'rb')
# video_bytes = video_file.read()
#
# st.video(video_bytes)

Age = st.number_input("Age of the customer")

# TAKE HEIGHT INPUT
# radio button to choose height format
Gender = st.radio('Gender: ',
				('Male', 'Female', 'Trans'))

Emptype=st.selectbox("EmpType:",['Private','Govt'])

	# compare status value

if( Gender== 'Male'):
# take height input in centimeters
	malesal = st.number_input('sal in between 50 to 100 thousand')

	try:
		avgsal = ((malesal / (12))*100)
	except:
		st.text("Enter sal greater than 10000")

elif(Gender == 'Female'):
# take height input in meters
	femalesal = st.number_input('eneter sal of both husband and wife')

	try:
		avgsal = ((femalesal / (10))*100)
	except:
		st.text("Enter sal greater than 10000")
else:
	st.text("Trans gender not eleigible")

# check if the button is pressed or not
if(st.button('Calculate Cibil')):

	# print the BMI INDEX
	st.text("Your avg sal is {}.".format(avgsal))

	# give the interpretation of BMI index
	if(avgsal <= 550):
		st.error("You are Extremely uneleigible")
	elif(avgsal > 550 and avgsal <= 650):
		st.warning("You need to improve cibil ")
	elif(avgsal >=650  and avgsal < 1000):
		st.success("you are eligible")
	else:
		st.text("no proper information")






