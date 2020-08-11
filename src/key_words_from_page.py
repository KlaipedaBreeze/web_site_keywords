import boto3
import trafilatura


def web_to_text(url):
    downloaded = trafilatura.fetch_url(url)
    return trafilatura.extract(downloaded)


def use_aws(text):
    client = boto3.client('comprehend', region_name='us-east-1')
    aws_result = client.batch_detect_entities(TextList=[text[:4000]], LanguageCode='en')
    unique_values = {}
    for x in aws_result['ResultList']:
        for y in x['Entities']:
            name = y['Text']
            enType = y['Type']
            if enType not in unique_values.keys():
                unique_values[enType] = []
            if name not in unique_values[enType]:
                unique_values[enType].append(name)
    return unique_values
