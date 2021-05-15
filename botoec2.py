import boto3
import json

#capn_compute
elasticcloudcompute = boto3.client( 'ec2',
	region_name='us-west-1',
	aws_access_key_id=AWS_KEY_ID,
	aws_secret_access_key=AWS_SECRET)

