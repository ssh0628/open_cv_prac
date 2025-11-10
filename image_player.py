import os
from PIL import Image
import cv2 as cv
import streamlit as st
import time

# Make File List
folder = "data"
file_list = os.listdir(folder)
playlist = []
ext = ['jpg', 'png', 'jpeg']
for file in file_list:
    if file.endswith(tuple(ext)):
        playlist.append(os.path.join(folder, file))

# Image Player
st.title("Image Player")
with st.container():
    canvas = st.empty()
    for i in range(len(playlist) - 1):
        one, two = 1.0, 0.0
        image1 = cv.resize(cv.imread(playlist[i]), (400, 400))
        image2 = cv.resize(cv.imread(playlist[i + 1]), (400, 400))       
        
        while two <= 1.0:
            dst = cv.cvtColor(cv.addWeighted(image1,one, image2, two, 0), cv.COLOR_BGR2RGB)
            one -= 0.01
            two += 0.01
            canvas.image(dst, width=400)
            time.sleep(0.01)

# Resize Function                
def image_resize():
    if image1.shape != image2.shape:
        height, width = min(image1.shape[0], image2.shape[0]), min(image1.shape[1], image2.shape[1])
        image1 = cv.resize(image1, (width, height))
        image2 = cv.resize(image2, (width, height))
