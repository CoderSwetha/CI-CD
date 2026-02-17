import boto3

def lambda_handler(event, context):
    s3_object = event['Records'][0]['s3']['object']['key']
    message = f"A new image named {s3_object} has been uploaded."
    # Send email via SES
    ses = boto3.client('ses')
    ses.send_email(
        Source='neelaswetha20@gmail.com',
        Destination={'ToAddresses': ['neelaswetha20@gmail.com']},
        Message={
            'Subject': {'Data': 'New Image Uploaded'},
            'Body': {'Text': {'Data': message}}
        }
    )
    return {"status": "success"}
