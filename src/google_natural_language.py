# Imports the Google Cloud client library
import os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'data\nlp-win-to-win-a56c00c219f6.json'

# Instantiates a client
client = language.LanguageServiceClient() #.from_service_account_json('nlp-win-to-win-687b51bbcc31.json')

def use_gcloud(text):
    # with open(trafiltext, 'r',  encoding="utf8") as file:
    #     text = file.read()
        # print(text)
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    # Detects the sentiment of the text

    # sentiment = client.analyze_sentiment(document=document).document_sentiment
    sdf = client.analyze_entities(document=document)
    # hhh = client.classify_text(document=document)
# 
    #print('Text: {}'.format(text))
    # print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    # print(hhh)
    print(sdf)
    return sdf
