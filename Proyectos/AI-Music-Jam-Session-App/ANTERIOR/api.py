from flask import Flask, render_template, request, send_file, make_response, jsonify
import uuid
import os  # For file path handling (replace with a secure storage mechanism)
import wave
import sys
import shutil
import random

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from audio_gen import goat

# **Crucial: Replace with a secure storage solution**
temp_file_folder = '/path/to/temporary/folder'  # Needs to be a secure location

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/new-audio')
def new_audio():
    return render_template('new-audio.html')
    



@app.route('/store-audio', methods=['POST'])
def store_audio():

    
    # Validate and process audio data (content type, size)
    # if not request.is_json:
    #     print("Cagaste")
    #     return 'Invalid request data', 400
    # print("pimba")

    audio_data = request.files.get("audio")
    print(audio_data)


    # return


    # # Assuming you have audio data in a blob (replace with your actual data)
    audio_blob = audio_data  # Your blob data

    audio_blob.save("uploaded-audio.mp3")

    goat("uploaded-audio.mp3")

    new_num = random.randint(1,10)
    shutil.copy("Goated.wav", f"loops/{new_num}.wav")





    # Create a new WAV file for writing
    # with wave.open('coutput.wav', 'wb') as wav_file:
    #     wav_file.setnchannels(1)  # Mono audio
    #     wav_file.setsampwidth(2)  # 16-bit samples
    #     wav_file.setframerate(44100)  # Sample rate (e.g., 44.1 kHz)
    #     wav_file.writeframes(audio_blob)

    # print("Audio written to coutput.wav")
    # print(new_num)
    data = {"message": "Success!", "data": new_num}
    response = make_response(jsonify(data))
    response.headers["Content-Type"] = "application/json"
    return response



@app.route('/get-audio/<num>', methods=["GET"])
def get_audio(num):
    print(f"route: {num}")
    path_to_file = f"../loops/{num}.wav"

    return send_file(
        path_to_file, 
        mimetype="audio/wav", 
        as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)




if __name__ == '__main__':
    app.run(debug=True)
