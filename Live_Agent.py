
import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
import cv2
import av
import os
import openai
from dotenv import load_dotenv
import base64
import streamlit as st
import openai
import io
from pydub import AudioSegment


# Load environment variables
# load_dotenv()


# Initialize the OpenAI API
def get_api():
    user_api_key = st.sidebar.text_input(
        label="OpenAI API key",
        placeholder="Paste your openAI API key here",
        type="password"
    )
    return user_api_key




# from pathlib import Path
# from openai import OpenAI
# client = OpenAI()

# def generate_audio(text):
#     response = client.audio.speech.create(
#         model="tts-1",
#         voice="alloy",
#         input=text
#     )
#     byte_stream = io.BytesIO(response.content)
#     return byte_stream

# WebRTC configuration for STUN server
RTC_CONFIGURATION = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

class VideoProcessor:
    def __init__(self):
        self.capture_frame = False
        self.image_saved = False
        self.image_path = ''

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        if self.capture_frame:
            self.image_path = 'captured_frame.png'
            cv2.imwrite(self.image_path, img)
            self.capture_frame = False
            self.image_saved = True

        return av.VideoFrame.from_ndarray(img, format="bgr24")

# Set up Streamlit page
st.set_page_config(page_title="LiveAgent")
st.title('LiveAgent')

# Set API Key
openai.api_key = get_api()
st.markdown("**Operation Explanation**")
# Instructions in English:
# "You can select the type of web camera or, if using a smartphone, the front or rear camera using the [SELECT DEVICE] button below. 
# If this is your first time, or if browser or smartphone permissions are prompted, please allow them before pressing [START]."
# "Press the [Capture Frame] button twice to start the API process and generate a description of the situation."

video_processor = VideoProcessor()
webrtc_ctx = webrtc_streamer(key="example", video_processor_factory=VideoProcessor, rtc_configuration=RTC_CONFIGURATION)

if webrtc_ctx.video_processor:
    if st.button("Capture Frame"):
        webrtc_ctx.video_processor.capture_frame = True

    if webrtc_ctx.video_processor.image_saved:
        if os.path.exists(webrtc_ctx.video_processor.image_path):
            st.image(webrtc_ctx.video_processor.image_path)
            with open(webrtc_ctx.video_processor.image_path, "rb") as img_file:
                base64_image = base64.b64encode(img_file.read()).decode("utf-8")

            with st.spinner('Sending request to OpenAI API...'):
                response = openai.chat.completions.create(
                    model="gpt-4-vision-preview",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                "Please explain specifically what you see there and what the situation is. Please be sure to use Japanese. No comments other than explanations are accepted.",
                                {"image": base64_image, "resize": 768},
                            ],
                        },
                    ],
                    max_tokens=500,
                )

            st.write(response.choices[0].message.content)
            # byte_stream = generate_audio(response.choices[0].message.content)
            # byte_stream.seek(0)
            # st.audio(byte_stream.read(), format="audio/mp3", autoplay=True)
            
            webrtc_ctx.video_processor.image_saved = False
        else:
            st.error(f"Image file not found: {webrtc_ctx.video_processor.image_path}")
            
st.markdown("**※This is a prototype and may frequently encounter errors or become unusable if the OpenAI API's usage limit is reached.**")

