import json
import boto3

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Employees')

def lambda_handler(event, context):

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(
        Bucket=bucket_name,
        Key=file_name
    )

    file_content = response['Body'].read().decode('utf-8')

    employee_data = json.loads(file_content)

    table.put_item(
        Item={
            'employee_id': employee_data['employee_id'],
            'name': employee_data['name'],
            'department': employee_data['department'],
            'salary': employee_data['salary']
        }
    )

    return {
        'statusCode': 200,
        'body': 'Data inserted successfully'
    }