import json
import random

def lambda_handler(event, context):
    request_body = json.loads(event['body'])
    text_input = request_body['userRequest']['utterance']

    rock_scissors_papers = ["가위", "바위", "보"]
    random_pick = rock_scissors_papers[random.randrange(0,3)]

    if not text_input in rock_scissors_papers:
        result = "잘못된 입력입니다. 가위, 바위, 보 중 하나를 입력하세요."
    if (text_input == "가위" and random_pick == "보") or (text_input == "바위" and random_pick == "가위") or (text_input == "보" and random_pick == "바위"):
        result = f"{random_pick}, 당신의 승리"
    elif (text_input == "가위" and random_pick == "바위") or (text_input == "바위" and random_pick == "보") or (text_input == "보" and random_pick == "가위"):
        result = f"{random_pick}, 당신의 패배"
    else:
        result = f"{random_pick}, 무승부"

    # https://kakaobusiness.gitbook.io/main/tool/chatbot/skill_guide/ai_chatbot_callback_guide#skillresponse
    return {
        'statusCode':200,
        'body': json.dumps({
            "version": "2.0",
            "template": { "outputs": [ { "simpleText": { "text": result } } ] }
        })
    }