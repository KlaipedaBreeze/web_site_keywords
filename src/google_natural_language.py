# Imports the Google Cloud client library
import os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'data/nlp-win-to-win-a56c00c219f6.json'
# Instantiates a client
client = language.LanguageServiceClient() #.from_service_account_json('nlp-win-to-win-687b51bbcc31.json')


def use_gcloud(text):
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    sdf = client.analyze_entities(document=document)
    unique_values = {}
    for entity in sdf.entities:
        name = entity.name
        enType = enums.Entity.Type(entity.type).name
        if enType not in unique_values.keys():
            unique_values[enType] = []
        if name not in unique_values[enType]:
            unique_values[enType].append(name)
    return unique_values
