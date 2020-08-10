import boto3
import json
from rake_nltk import Rake
import trafilatura


def web_to_text(url):
    downloaded = trafilatura.fetch_url(url)
    return trafilatura.extract(downloaded)


def use_aws(text):
    client = boto3.client('comprehend', region_name='us-east-1')
    aws_result = client.batch_detect_entities(TextList=[text[:4000]], LanguageCode='en')
    print(aws_result.keys())
    print(aws_result['ResultList'])
    unique_values = {}

    for x in aws_result['ResultList']:
        print(x)

        # if enType not in unique_values.keys():
        #     unique_values[enType] = []
        # if name not in unique_values[enType]:
        #     unique_values[enType].append(name)
    return unique_values



# def exctract_text(text):
#     r = Rake(min_length=1, max_length=2)
#     # Uses stopwords for english from NLTK, and all puntuation characters.
#     r.extract_keywords_from_text(text)
#     rankeds = r.get_ranked_phrases()
#
#     for word in rankeds:
#         print(word)

