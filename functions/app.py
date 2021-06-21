import boto3
import json
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']

def lambda_handler(event, context):
    table = dynamodb.Table(table_name)
    if event['httpMethod'] == 'GET':
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "presenq getA" + str(event['pathParameters']['board_id']),
            }),
        }
    elif event['httpMethod'] == 'POST':
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "presenq post",
            }),
        }
    else:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "presenq error",
            }),
        }
