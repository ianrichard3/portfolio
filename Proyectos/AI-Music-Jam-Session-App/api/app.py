from flask import Flask, render_template, request, send_file, make_response, jsonify
import os
import sys
import shutil
import random



app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)