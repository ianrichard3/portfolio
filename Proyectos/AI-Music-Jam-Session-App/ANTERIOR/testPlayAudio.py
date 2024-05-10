from flask import Flask, render_template, request, send_file, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('play-audio.html')


@app.route('/get-audio', methods=["GET"])
def get_audio():
     path_to_file = "goaty.wav"

     return send_file(
         path_to_file, 
         mimetype="audio/wav", 
         as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)