import json
import datetime
import requests

url = "http://uname.link/slack/log"
def handler(event, context):
    data = event
    keywords = ['Message', 'body']
    code = 200
    try:
         for key in keywords:
            if key in event:
                data = event[key]
                break

    except Exception as e:
        data = str(e)
        print(str(e))
        code = 500
    finally:
        print("-------------")
        print(data)
        print("-------------")

    r = requests.post(url, data=json.dumps(data))
    print(r.content)

    return {'statusCode': code,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
