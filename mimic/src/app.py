import json

def lambda_handler(event, context):
    request_body = json.loads(event['body'])
    user_message = request_body['userRequest']['utterance']

    # https://kakaobusiness.gitbook.io/main/tool/chatbot/skill_guide/ai_chatbot_callback_guide#skillresponse
    return {
        'statusCode':200,
        'body': json.dumps({
            "version": "2.0",
            "template": { "outputs": [ { "simpleText": { "text": f"🦜 {user_message}" } } ] }
        })
    }