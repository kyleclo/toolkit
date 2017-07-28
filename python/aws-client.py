import os
import pandas as pd
import boto3
from StringIO import StringIO

def read_from_s3(s3_bucket, s3_dirpath, input_filename):
    """Reads csv file directly from S3 into pandas dframe"""
    s3_client = boto3.client('s3')
    obj = s3_client.get_object(Bucket=s3_bucket,
                               Key=os.path.join(s3_dirpath, input_filename))
    str = obj['Body'].read()
    df = pd.read_csv(StringIO(str))
    return df

def write_to_s3(df, s3_bucket, s3_dirpath, output_filename):
    """Writes pandas dframe directly to csv file in s3"""
    s3_client = boto3.client('s3')
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_client.put_object(Bucket=s3_bucket,
                         Key=os.path.join(s3_dirpath, output_filename),
                         Body=csv_buffer.getvalue())
