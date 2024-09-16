import json
import requests
from datetime import date

def lambda_handler(event, context):
    today = date.today().strftime("%Y-%m-%d") # "2024-09-17"
    url = f"https://api.popply.co.kr/api/store/?fromDate={today}&toDate={today}"
    response = requests.get(url)
    data = response.json()

    # https://kakaobusiness.gitbook.io/main/tool/chatbot/skill_guide/ai_chatbot_callback_guide#skillresponse
    return {
        'statusCode':200,
        'body': json.dumps({
            "version": "2.0",
            "template": { "outputs": [ { "simpleText": { "text": f'Hello World' } } ] }
        })
    }