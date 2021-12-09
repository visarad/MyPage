import boto3

aws_mag_con = boto3.session.Session()

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

data = open('loan.csv', 'rb')
try:
    s3.Bucket('visarad').put_object(Key='loan.csv', Body=data)
    print('Successfully sent to s3')
except:
    print('Unable to send to s3 bucket')

