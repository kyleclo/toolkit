import os
import pandas as pd
import boto3
from StringIO import StringIO

# simple example

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

# complex example

class FileContext(object):
    def read_df(self):
        raise NotImplementedError

    def write_df(self, out_df):
        raise NotImplementedError


class LocalFileContext(FileContext):
    def __init__(self, input_filepath, output_filepath):
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath

    def read_df(self):
        return pd.read_csv(self.input_filepath)

    def write_df(self, out_df):
        out_df.to_csv(self.output_filepath, index=False)


class S3FileContext(FileContext):
    def __init__(self, s3_bucket, s3_input_filepath, s3_output_filepath):
        self.s3_bucket = s3_bucket
        self.s3_input_filepath = s3_input_filepath
        self.s3_output_filepath = s3_output_filepath

    def read_df(self):
        """Reads csv file directly from S3 into pandas dframe"""

        s3_client = boto3.client('s3')
        obj = s3_client.get_object(Bucket=self.s3_bucket,
                                   Key=self.s3_input_filepath)
        str = obj['Body'].read()
        df = pd.read_csv(StringIO(str))
        return df

    def write_df(self, out_df):
        """Writes pandas dframe directly to csv file in s3"""

        s3_client = boto3.client('s3')
        csv_buffer = StringIO()
        out_df.to_csv(csv_buffer, index=False)
        s3_client.put_object(Bucket=self.s3_bucket,
                             Key=self.s3_output_filepath,
                             Body=csv_buffer.getvalue())
    
if is_local:
    file_context = LocalFileContext(...)
elif is_s3:
    file_context = S3FileContext(...)
else:
    raise Exception

in_df = file_context.read_df()
file_context.write_df(out_df)
