import streamlit as st
import yt_dlp
import sys
import os

try:
    st.set_page_config('Video AutoTranslator')
    st.title('Video AutoTranslator')
    url = st.text_input('Youtube URL', placeholder='https://youtube.com/watch/v/fdsahfdesaf')
    button = st.button('Submit')

    if button and url:
        ydl_opts = {
            'format': 'wav/bestaudio/best',
            'outtmpl': 'audio',
            'postprocessors': [{  # Extract audio using ffmpeg
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(url) 
            
        with open(os.path.join(os.curdir, 'audio.wav'), 'rb') as audio_file:
            st.audio(audio_file.read(), format='audio/wav')

except KeyboardInterrupt:
    sys.exit(1)
except Exception as e:
    print(str(e))
