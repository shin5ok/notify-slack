import json
import datetime
import requests

url = "http://t2.uname.link/slack/kawano"
def handler(event, context):
    try:
        data = json.loads(event)['body']
    except Exception as e:
        print(str(e))
        data = event.get('body')
    finally:
        print("-------------")
        print(data)
        print("-------------")

    r = requests.post(url, data=data)
    print(r.content)

    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
