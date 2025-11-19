#!/usr/bin/env python3

import boto3
import requests
import os

def df(url, path):
	try:
        	response = requests.get(url, stream=True)
        	response.raise_for_status()

	        with open(path, 'wb') as i_file:
        		for chunk in response.iter_content(chunk_size=8192):
                		i_file.write(chunk)
        	print(f"File downloaded to {path}")
	except requests.exceptions.RequestException as e:
        	print(f"Error downloading: {e}")

# create client
s3 = boto3.client('s3', region_name="us-east-1")

my_url = "https://www.discoverboating.com/sites/default/files/Sailboat-Types_1.jpg"
file = "new_image.jpg"
file_path = os.path.join(os.getcwd(), file)

df(my_url,file_path)
# make request
response = s3.list_buckets()

bucket = 'ds2002-f25-jrn2kf'

local_file_path = file_path

s3_key = 'new_image.jpg'

s3.upload_file(Filename=local_file_path, Bucket=bucket, Key=s3_key)

print("Upload Successful")

expires = 604800

true_url = s3.generate_presigned_url('get_object',Params={'Bucket': bucket, 'Key': s3_key}, ExpiresIn=expires)
print(true_url)
