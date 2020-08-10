# Imports the Google Cloud client library
import os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import itertools


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'data/nlp-win-to-win-a56c00c219f6.json'

# Instantiates a client
client = language.LanguageServiceClient() #.from_service_account_json('nlp-win-to-win-687b51bbcc31.json')


def use_gcloud(text):
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    # Detects the sentiment of the text
    # #sentiment = client.analyze_sentiment(document=document).document_sentiment
    sdf = client.analyze_entities(document=document)

    unique_values = {}
    list_of_values = []
    # Loop through entitites returned from the API
    for entity in sdf.entities:
        # print(u"Representative name for the entity: {}".format(entity.name))
        # print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
        # print(u"Salience score: {}".format(entity.salience))
        for metadata_name, metadata_value in entity.metadata.items():
            # print(u"{}: {}".format(metadata_name, metadata_value))
            for mention in entity.mentions:
                # print(u"Mention text: {}".format(mention.text.content))
                # print(u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name))
                if enums.EntityMention.Type(mention.type).name in unique_values.keys():
                    pass
                else:
                    unique_values[enums.EntityMention.Type(mention.type).name] = len(unique_values)
                    if unique_values.values() in list_of_values:
                        pass
                    else:
                        list_of_values.append([len(unique_values) - 1])
                for key in unique_values.keys():
                    if enums.EntityMention.Type(mention.type).name != key:
                        pass
                    else:
                        list_of_values[unique_values.get(key)].append(mention.text.content)
    unique_list = []
    inv_map = {v: k for k, v in unique_values.items()}
    for uno_listo in list_of_values:
        unique_list.append(list(set(uno_listo)))
    for list_number in unique_list:
        if inv_map.get(list_number[0]) is not None:
            list_number[0] = '***' + inv_map.get(list_number[0]) + '***'
        else:
            list_number[0] = inv_map.get(list_number[0])
        print(inv_map.get(list_number[0]))
        print(list_number[0])
    res = str(unique_list)
    res = res.replace(']', '<br>')
    res = res.replace(' [', '')
    res = res.replace('[', '')
    res = res.replace(',', '')
    res = res.replace("'", "")
    print(res)
    return res
            # hhh = client.classify_text(document=document)
    #print('Text: {}'.format(text))
    # print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    # print(hhh)
    # print(sdf)
