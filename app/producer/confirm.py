import json
import os
import boto3

def lambda_handler(event, context):
try:
    message_id = event['message_id']
    response = retrieve_message(message_id)
except Exception as e:
    print('Exception Message: ' + str(e))
    print("Message wasn't registered: " + queue_name)
    return {
    'statusCode': 500,
    'body': json.dumps('Internal Server Error')
    }
if 'Item' in response:
    return {
    'statusCode': 200,
    'body': json.dumps(response['Item'])
    }
else:
    return {
    'statusCode': 404,
    'body': json.dumps('Not Found')
    }

def retrieve_message(message_id):
table_name = os.environ['TABLE_NAME']
dynamoDB = boto3.resource('dynamodb')
table= dynamoDB.Table(table_name)
response = table.get_item(
    Key={
    'EventId': message_id
    }
    )

return response