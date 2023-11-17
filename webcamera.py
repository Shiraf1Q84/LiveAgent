import streamlit as st
from streamlit_webrtc import webrtc_streamer

# RTC Configuration for WebRTC streamer to use Google's STUN server
RTC_CONFIGURATION = {
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
}

def main():
    # Set up the main page
    st.title("My first Streamlit app")
    st.write("Hello, world")

    # Start the WebRTC streamer with the specified RTC configuration
    webrtc_streamer(key="example", rtc_configuration=RTC_CONFIGURATION)

if __name__ == "__main__":
    main()
