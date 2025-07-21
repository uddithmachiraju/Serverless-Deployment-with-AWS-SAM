import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "response": "Hello from lambda" 
    }