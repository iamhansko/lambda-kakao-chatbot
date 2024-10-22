import json
import boto3

def lambda_handler(event, context):  
    request_body = json.loads(event['body'])
    lambda_client = boto3.client('lambda')
    lambda_client.invoke(
        FunctionName="callback",
        InvocationType='Event',
        Payload=json.dumps({
            'prompt' : request_body['userRequest']['utterance'],
            'callback_url' : request_body['userRequest']['callbackUrl']
        })
    )

    return {
        'statusCode':200,
        'body': json.dumps({
            'version': '2.0',
            'useCallback' : True,
            'data': { 'text' : '' }
        })
    }