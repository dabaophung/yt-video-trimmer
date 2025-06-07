import streamlit as st
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

st.title("🎬 YouTube Video Trimmer")

url = st.text_input("Paste YouTube URL here:")
start_time = st.number_input("Start time (in seconds):", min_value=0)
end_time = st.number_input("End time (in seconds):", min_value=0)

if st.button("Trim Video"):
    if url and end_time > start_time:
        try:
            st.info("Downloading video...")
            yt = YouTube(url)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            video_path = stream.download(filename="video.mp4")

            st.success("Downloaded. Now trimming...")

            trimmed_path = "trimmed_video.mp4"
            clip = VideoFileClip(video_path).subclip(start_time, end_time)
            clip.write_videofile(trimmed_path, codec="libx264")

            st.success("Trimming complete! Download below:")
            with open(trimmed_path, "rb") as file:
                st.download_button("Download Trimmed Video", file, file_name="trimmed_video.mp4")

            clip.close()
            os.remove(video_path)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid URL and time range.")
