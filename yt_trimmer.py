{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
from pytube import YouTube\
from moviepy.editor import VideoFileClip\
import os\
\
st.title("\uc0\u55356 \u57260  YouTube Video Trimmer")\
\
url = st.text_input("Paste YouTube URL here:")\
start_time = st.number_input("Start time (in seconds):", min_value=0)\
end_time = st.number_input("End time (in seconds):", min_value=0)\
\
if st.button("Trim Video"):\
    if url and end_time > start_time:\
        try:\
            st.info("Downloading video...")\
            yt = YouTube(url)\
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()\
            video_path = stream.download(filename="video.mp4")\
\
            st.success("Downloaded. Now trimming...")\
\
            trimmed_path = "trimmed_video.mp4"\
            clip = VideoFileClip(video_path).subclip(start_time, end_time)\
            clip.write_videofile(trimmed_path, codec="libx264")\
\
            st.success("Trimming complete! Download below:")\
            with open(trimmed_path, "rb") as file:\
                st.download_button("Download Trimmed Video", file, file_name="trimmed_video.mp4")\
\
            clip.close()\
            os.remove(video_path)\
\
        except Exception as e:\
            st.error(f"Error: \{e\}")\
    else:\
        st.warning("Please enter a valid URL and time range.")}