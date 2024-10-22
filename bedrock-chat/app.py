import asyncio
import json
import os
from langchain_aws import ChatBedrock

# https://python.langchain.com/docs/integrations/llms/bedrock/
def bedrock_chatbot(input_text):
    bedrock_llm = ChatBedrock(
        credentials_profile_name='default',
        model_id='anthropic.claude-3-5-sonnet-20240620-v1:0',
        model_kwargs={
            "temperature": 0.5,
            "top_p": 1,
            "top_k": 250,
            "max_tokens": 512
        }
    )
    # return bedrock_llm.predict(input_text)
    return bedrock_llm.invoke([("human", input_text)])

async def delayed_print():
    await asyncio.sleep(4)
    # response = bedrock_chatbot(user_message)
    # https://kakaobusiness.gitbook.io/main/tool/chatbot/skill_guide/ai_chatbot_callback_guide#skillresponse
    # print(response.content)
    print(5)

async def main():
    # request_body = json.loads(event['body'])
    # print(event)
    # print(context)
    # print(request_body)
    # user_message = request_body['userRequest']['utterance']

    task = asyncio.create_task(delayed_print())

    return {
        'statusCode':200,
        'body': json.dumps({
            'version': '2.0',
            'useCallback' : True,
            'data': { 'text' : '생각하고 있는 중이에요😘 \n15초 정도 소요될 거 같아요 기다려 주실래요?!' }
        })
    }, await task

    # response.content

def lambda_handler(event, context):
    result, _ = asyncio.run(main())
    return result