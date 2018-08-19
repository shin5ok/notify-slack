import json
import datetime
import requests

url = "http://t2.uname.link/slack/kawano"
def handler(event, context):
    data = event
    keywords = ['Message', 'body']
    try:
         for key in keywords:
            if key in event:
                data = event[key]
                break

    except Exception as e:
        data = str(e)
        print(str(e))
    finally:
        print("-------------")
        print(data)
        print("-------------")

    r = requests.post(url, data=data)
    print(r.content)

    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
