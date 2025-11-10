import streamlit as st
import cv2 as cv

st.title("Cat")
img_path = "cat.png"
# img = cv.imread(img_path, flags=cv.IMREAD_GRAYSCALE)
col1, col2 = st.columns(2)

with col1:
    st.image("cat.png", caption="original image")
with col2:
    img = cv.imread(img_path, flags=cv.IMREAD_GRAYSCALE)
    st.image(img, caption="gray scale image")


file_name = st.text_input("Press Enter to continue...")
def save_image(file_name):
    if file_name:
        cv.imwrite(file_name, img)
        st.success(f"Image save as {file_name}")
    
st.button("Save", key="save", on_click=save_image, args=(file_name,))