import boto3

ec2 = boto3.resource('ec2')#ami-07b068f843ec78e72

ec2.create_instances(ImageId='ami-07b068f843ec78e72', MinCount=1, MaxCount=1)

i-0c038a32956019acc

response = ec2.describe_key_pairs()
print(response)

