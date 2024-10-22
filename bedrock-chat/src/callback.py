import json
import os
import requests
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
    return bedrock_llm.invoke([("human", input_text)])

def lambda_handler(event, context):
    response = bedrock_chatbot(event['prompt'])
    callback_url = event['callback_url']

    # https://kakaobusiness.gitbook.io/main/tool/chatbot/skill_guide/ai_chatbot_callback_guide#skillresponse
    requests.post(callback_url, json={
        "version": "2.0",
        "useCallback": False,
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": f"{response}"
                    }
                }
            ]
        }
    })

    return True