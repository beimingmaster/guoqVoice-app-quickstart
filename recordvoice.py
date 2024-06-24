import streamlit as st
from st_audiorec import st_audiorec
import os

wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    # 播放录制的音频
    st.audio(wav_audio_data, format='audio/wav')
    
    # 保存音频到本地
    save_path = "recorded_audio.wav"
    with open(save_path, "wb") as f:
        f.write(wav_audio_data)
    
    st.success(f"音频已保存到: {os.path.abspath(save_path)}")