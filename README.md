# Personal-Pet-Robot 
<img src="https://github.com/Pglol03/Personal-Pet-Robot/blob/master/Images/07-eyes_front.png" alt="RobotEyes.jpg" width="128" height="64 /> 
[Robot Eyes]

Project Area : Artificial Intelligence, Virtual Assistant, Prompt Engineering, Multi-threading


## Author

- [@Pradyun Gayakwad](https://www.github.com/Pglol03)


## Description:
The whole program runs on queries and multithreading concepts are implemented within its modules with package functions being called in the main function. Altogether there are 12 packages whose descriptions are as follows:

### Hardware interface packages

#### Display.py
- Used to interface and perform custom animation on the old display attached.

#### IR_Sensor.py
- It checks the input of IR Sensor from the GPIO pins in order to prevent run-aways and falling over from surfaces

#### PPR.py(Main func)
- This is the main function the initiates the robot and calls all the necessary functions too that they work together harmoniously.

### Software interface packages

#### Speech.py
- Takes text input and converts it to voice(audio) output to the speaker

#### Recognition.py
- Takes audio input and transcribes it into text

#### Commands.py
- Runs the transcribes audio here to check what actions to perform for the voice inputs

#### Cmdline.py
- Runs the ‘pushtotalk’ google assistant api for web search for the query requested by the user.

### Google assistant packages:

#### Pushtotalk.py
- Main program to transcribe audio, send request to api, authentication of device, storing all the tokens and keys required for api handshake and return the result from the api and audio output

#### assistant_helpers.py
- It provides helper functions for the google assistant API

#### audio_helpers.py
- It provides helper function for audio streams and audio setup and error handling.

#### browser_helpers.py
- It provides the function to write the request to the API in html request.

#### device_helpers.py
- Its provides helper function for the device in case we want to perform some custom actions through the google assistant API.

## Libraries Used

### Hardware interface 
- Board
- Digital
- Pil
- adafruit_ssd1306
- RPi.GPIO

### Supporting software libraries
- Time
- speech_recognition
- Pyttsx3
- Google assistant api
- embedded_assistant_pb2
- Logging
- Array
- Logging
- Math
- Time
- Threading
- Wave
- Click
- Sound device
- Os.path
- Tempfile
- Webbrowser
- Subprocess
- concurrent.futures
- Sys
- Json
- Os
- Pathlib2
- Uuid
- Grace
- Google.auth.transport.grpc
- Google.auth.transport.requests
- Google.oauth2.credentials
- Embedded_assistant_pb2_grpc
- Tenacity

## Installation

Execute these commands in the project directory terminal.

```bash
  source venv/bin/activate
  python3 Image_Stitching.py 
```
Go [here](./input/p4/results) for more intermediate results for all image pairs

