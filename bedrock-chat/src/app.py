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
            "max_tokens": 128
        }
    )
    return bedrock_llm.invoke([("human", input_text)])

def lambda_handler(event, context):
    request_body = json.loads(event['body'])
    text_input = request_body['userRequest']['utterance']
    response = bedrock_chatbot(text_input)

    # https://kakaobusiness.gitbook.io/main/tool/chatbot/skill_guide/ai_chatbot_callback_guide#skillresponse
    return {
        'statusCode':200,
        'body': json.dumps({
            'version': '2.0',
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": f"{response.content}"
                        }
                    }
                ]
            }
        })
    }