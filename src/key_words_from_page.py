# import web_to_text as wt
import boto3
import json
from rake_nltk import Rake
import trafilatura


def web_to_text(url):
    downloaded = trafilatura.fetch_url(url)
    # print(downloaded)
    return trafilatura.extract(downloaded)

# text = web_to_text("http://adrien.barbaresi.eu/blog/trafilatura-main-text-content-python.html")

def use_aws(text):
    client = boto3.client('comprehend')
    aws_result = client.batch_detect_key_phrases(TextList=[text[:4000]], LanguageCode='en')

# print(aws_result)

def exctract_text(text):
    r = Rake(min_length=1, max_length=2)
    # Uses stopwords for english from NLTK, and all puntuation characters.
    r.extract_keywords_from_text(text)
    rankeds = r.get_ranked_phrases()

# for word in rankeds:
#     print(word)

