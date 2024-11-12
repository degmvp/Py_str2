import streamlit as st
import pandas as pd
import numpy as np
import time
from faker import Faker
import matplotlib.pyplot as plt
import turtle
import math
from PIL import Image, ImageFilter, ImageOps
import os

# Sidebar
st.sidebar.header('Menu')
selected_menu = st.sidebar.selectbox('Choose an option', ['Op 1', 'Op 2', 'Op 6','Op 7','Op 8','Op 9',])

# Main content
st.header('Python Streamlit App ')
st.text('Media Player -  Mp3 - Mp4 - Images')
st.text('Sidebar and Selectbox')

if selected_menu == 'Op 1':
    st.write('Menu Op 1. - Play MP3 file')
elif selected_menu == 'Op 2':
    st.write('Menu Op 2. - Play Video MP4 file')
elif selected_menu == 'Op 6':
    st.write('Menu Op 6. backup Y-PYMP34.py to C:\ R:\ ')
elif selected_menu == 'Op 7':
    st.write('Menu Op 7. exibe a foto dondeg ')
elif selected_menu == 'Op 8':
    st.write('Menu Op 8. exibe a foto lawrence')
elif selected_menu == 'Op 9':
    st.write('Menu Op 9. exibe funcoes streamlit')


def exec_trick1():
    st.title("Media Player")
    st.header("Audio Player")

    # Directory containing the audio files
    audio_dir = r"E:\Y-PYVMEDIA"

    # List all mp3 files in the directory
    audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.mp3')]

    # Selectbox for choosing an audio file
    selected_audio = st.selectbox('Choose an audio file', audio_files)

    # Read and play the selected audio file
    audio_path = os.path.join(audio_dir, selected_audio)
    audio_file = open(audio_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
exec_trick1()
# Link the CSS file
st.markdown('<link rel="stylesheet" href="style.css">', unsafe_allow_html=True)
# Execute the function




def exec_trick2(video_file_path):
    st.header("Video Player")
    with open(video_file_path, 'rb') as video_file:
        video_bytes = video_file.read()
        st.video(video_bytes)

# Get list of video files
video_dir = r"E:\Y-PYVMEDIA"
video_files = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]

# Combo box to select video file
selected_video = st.selectbox('Choose a video file', video_files)

# Button to trigger trick2
if st.button('exec Video'):
    video_path = os.path.join(video_dir, selected_video)
    exec_trick2(video_path)

def exec_backup():
        import shutil
        source=r'E:\\Y-PYVMEDIA\\Y-PYMP34.py'
        destination=r'R:\XPYTOOLV1\Y-PYMP34.py'
        shutil.copyfile(source, destination)
        print('backup Y-PYMP34.PY ==> R:\XPYTOOLV1')
        #--------------------------------------------
        source=r'E:\\Y-PYVMEDIA\\Y-PYMP34.py'
        destination='C:\\BACKUP\Y-PYMP34.py'
        shutil.copyfile(source, destination)
        print('backup Y-PYMP34.py ==> C:\BACKUP')
        #------------------------------------------

# Button to trigger trick6
if st.button('exec backup'):
    exec_backup()

def exec_show_img():
    st.title("Display Image")
    # Path to the image file
    image_path = "don.jpg"  # Update this with the correct path to your image file

    try:
        # Read the image file and display it
        with open(image_path, "rb") as f:
            image_bytes = f.read()
            st.image(image_bytes, caption='Degmar', width=150)
    except FileNotFoundError:
        st.error("Image file not found. Please check the file path.")

# Button to trigger trick4
if st.button('exec Deg'):
    exec_show_img()

def exec_show_nir():
    st.title("Display Image")
    # Path to the image file
    image_path = "law.jpg"  # Update this with the correct path to your image file

    try:
        # Read the image file and display it
        with open(image_path, "rb") as f:
            image_bytes = f.read()
            st.image(image_bytes, caption='Law-meu-filho', width=150)
    except FileNotFoundError:
        st.error("Image file not found. Please check the file path.")

# Button to trigger trick4
if st.button('exec Law'):
    exec_show_nir()

chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
                             
def exec_trick9():
     st.success("This is a success message!")
     st.error("This is an error message!")
     st.warning("This is a warning message!")
     st.info("This is an info message!")

     st.title('Interactive Widgets')

     st.button('Hi! Deg')
     st.write('Hi, Streamlit!')
     time.sleep(3)  # Pause for 3 seconds

     st.write('Pause complete 3 seconds')

     st.text_input('Degmar Gomes Barbosa')


     st.title('Line Chart Example')
     st.line_chart(chart_data)

if st.button('exec trick9'):
    exec_trick9()

