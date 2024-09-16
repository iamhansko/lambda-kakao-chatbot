import json
import requests

def lambda_handler(event, context):
    url = "https://dksh.awskorea.kr"
    response = requests.get(url)
    data = response.json()

    # https://kakaobusiness.gitbook.io/main/tool/chatbot/skill_guide/ai_chatbot_callback_guide#skillresponse
    return {
        'statusCode':200,
        'body': json.dumps({
            "version": "2.0",
            "template": { "outputs": [ { "simpleText": { "text": f'{data["menu"]} ([이미지]({data["image"]}))' } } ] }
        })
    }