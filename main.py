from flask import Flask, request, render_template
import pathlib
import requests
import trafilatura
from src.key_words_from_page import web_to_text
from src.google_natural_language import use_gcloud
from src.key_words_from_page import use_aws

    
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    url = request.form['text']
    response = web_to_text(url)
    aws_result = use_aws(response)
    gcloud_result = use_gcloud(response)


    return response

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')