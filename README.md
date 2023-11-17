# Real-Time Commentary Web App

## Overview
This web application is designed to capture images from a web camera, generate a commentary based on the image using OpenAI's GPT-4 model, and convert this commentary into audio. It utilizes Streamlit for the web interface, `streamlit_webrtc` to capture the camera stream, `openai` for the GPT-4 API calls, and `pydub` to handle audio stream conversion.

## Features
- Real-time video streaming from a web camera.
- Image capture and saving functionality.
- Integration with OpenAI's GPT-4 model for image-based commentary generation.
- Real-time audio generation from the commentary text.
- WebRTC configuration for STUN server to handle video streaming.
  
## How to Use
1. Clone this repository to your local machine.
2. Install the required dependencies from `requirements.txt`.
3. Run the Streamlit app.
4. Input your OpenAI API key in the sidebar.
5. Start the video stream and capture an image.
6. Wait for the app to generate and display the commentary.
7. Listen to the generated audio commentary.

## Instructions
- Use the [SELECT DEVICE] button to choose the camera type or, on a smartphone, switch between the front and rear cameras.
- If this is your first time, or if permissions are required by the browser or smartphone, please grant them before pressing [START].
- Double-click the [Capture Frame] button to initiate the API process and generate a description of the situation.

## Important Notes
- The app is a prototype and may encounter errors or become unusable if the OpenAI API's usage limit is reached.
- Please ensure you have the necessary permissions to use the web camera on your device.
- The commentary and audio are generated based on the captured image and are presented in Japanese.

## Dependencies
- streamlit
- streamlit_webrtc
- opencv-python (cv2)
- av
- openai
- python-dotenv
- base64
- pydub

## Configuration
- A `.env` file is required to store environment variables such as the OpenAI API key.
- A `RTC_CONFIGURATION` is set up for the STUN server to facilitate video streaming.

## Files
- `app.py`: The main application script.
- `.env.example`: An example `.env` file.
- `requirements.txt`: Required Python libraries.

## How to Run
Ensure you have Python installed and then set up a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install dependencies:

```sh
pip install -r requirements.txt
```

Start the app:

```sh
streamlit run app.py
```

## Contribution
Feedback and contributions are welcome. Please create an issue or pull request on the repository if you would like to contribute.

## License
Please refer to the repository's license for usage guidelines.

## Contact
For support or further information, please contact the repository maintainer.

---
