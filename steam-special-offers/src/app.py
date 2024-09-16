import json
import requests

def lambda_handler(event, context):
    url = "https://store.steampowered.com/api/featuredcategories?l=korean"
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