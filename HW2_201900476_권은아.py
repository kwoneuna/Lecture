import streamlit as st
from PIL import Image
import numpy as np
from PIL import ImageOps
from PIL import ImageFilter

st.set_page_config(layout='wide',page_title='My DIP')
st.write('### Homework 2 권은아')
st.write(':cat:')
st.sidebar.write('## my sidebar')

def process_image(upload):
    image = Image.open(upload)
    col1.write('Input')
    col1.image(image)
    
    #Gray scale로 변환
    gray = image.convert('L')
    col2.write('Output 1 : Gray')
    col2.image(gray)

    #HistEqualize 수행
    I_eq = ImageOps.equalize(image)
    col3.write('Output 2 : Histeq')
    col3.image(I_eq)

    #Gaussian blur
    img_blur = image.filter(ImageFilter.GaussianBlur(10))
    col4.write('Output 3 : My own processing')
    col4.image(img_blur)




col1,col2,col3,col4 = st.columns(4)
my_upload = st.sidebar.file_uploader('Upload',type=['png','jpeg','jpg'])

if my_upload is not None:
    process_image(upload=my_upload)
else:
    process_image('./pudding.jpeg')

