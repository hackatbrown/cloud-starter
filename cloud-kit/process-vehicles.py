import json
import boto3
import csv
import io

# Create an S3 client using the boto3 library
s3Client = boto3.client('s3')

def lambda_handler(event, context):
   # Log a message to the console to indicate that the Lambda function has started
   print("Hello world")
   
   # Retrieve the bucket name and object key (file name) from the event
   # This event is triggered when a new file is uploaded to an S3 bucket
   bucket = event['Records'][0]['s3']['bucket']['name']  # Name of the S3 bucket
   key = event['Records'][0]['s3']['object']['key']      # Key (file path) of the uploaded file
   
   # Print bucket and key values for debugging purposes
   print(bucket)
   print(key)
   
   # Fetch the uploaded file (S3 object) from the specified bucket using the key (file path)
   obj = s3Client.get_object(Bucket=bucket, Key=key)
   
   # Read the file content and decode it from bytes to a UTF-8 string
   data = obj['Body'].read().decode('utf-8')
   
   # Create a CSV reader to parse the file content
   # io.StringIO is used to treat the string as a file-like object for the CSV reader
   reader = csv.reader(io.StringIO(data))
   
   # Skip the first row (header) if present in the CSV file
   next(reader)
   
   # Loop through the rows of the CSV file and print the values in a formatted way
   # Assumes that each row contains three values: Year, Mileage, and Price
   for row in reader:
       print(str.format("Year - {}, Mileage - {}, Price - {}", row[0], row[1], row[2]))