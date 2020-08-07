import boto3
import json

#comprehend = boto3.client(service_name='comprehend', region_name='eu-north-1')

client = boto3.client('comprehend')
text = "Why do people shop? People shop because they’re looking for solutions to their problems. They need something to improve their lives that they couldn’t otherwise do or achieve without your product. Show people the ideal versions of themselves. Use product descriptions to paint a before-and-after picture. To see the copywriting formula AppSumo uses to write product descriptions that make $250,000+ in 7-10 days"

response = client.batch_detect_dominant_language(
    TextList=[
        text
    ]
)

print(json.dumps(response, sort_keys=True, indent=4))

print(json.dumps(client.detect_sentiment(Text=text, LanguageCode='en'),
                 sort_keys=True, indent=4))

print(json.dumps(client.batch_detect_key_phrases(TextList=[text], LanguageCode='en'),
                 sort_keys=True, indent=4))


print(json.dumps(client.batch_detect_key_phrases(TextList=[text], LanguageCode='en'),
                 sort_keys=True, indent=4))

print(json.dumps(client.batch_detect_entities(TextList=[text], LanguageCode='en'),
                 sort_keys=True, indent=4))

#print('Calling DetectSentiment')
#print(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'),
#                 sort_keys=True, indent=4))
#print('End of DetectSentiment\n')
