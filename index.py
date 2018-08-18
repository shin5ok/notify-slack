import json
import datetime
import requests

def handler(event, context):
    data = event
    requests.post(url, data=data)

    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
