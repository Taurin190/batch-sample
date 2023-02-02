import json
import os
import boto3

def lambda_handler(event, context):
try:
    message_id = send_message_to_sqs(message='Hello')
except Exception as e:
    print('Exception Message: ' + str(e))
    print("Message wasn't sent: " + queue_name)
    return {
    'statusCode': 500,
    'body': json.dumps('Internal Server Error')
    }

try:
    register_message_id(message_id)
except Exception as e:
    print('Exception Message: ' + str(e))
    print("Message wasn't registered: " + queue_name)
    return {
    'statusCode': 500,
    'body': json.dumps('Internal Server Error')
    }
result = {'message_id': message_id};

return {
    'statusCode': 200,
    'body': json.dumps(result)
}

def send_message_to_sqs(message):
queue_name = os.environ['QUEUE_NAME']
sqs = boto3.client("sqs", endpoint_url="https://sqs.ap-northeast-1.amazonaws.com")

response = sqs.get_queue_url(QueueName=queue_name)
queue_url = response['QueueUrl']

response = sqs.send_message(QueueUrl=queue_url, MessageBody='Hello')
return response['MessageId']

def register_message_id(message_id):
table_name = os.environ['TABLE_NAME']
dynamoDB = boto3.resource('dynamodb')
table= dynamoDB.Table(table_name)
table.put_item(
    Item = {
    'EventId': message_id,
    'Status': 'CREATED'
    }
    )

return