import boto3
import os


def download_all_file_in_folder(bucket_name):
    for obj in bucket.objects.all():
        dest = obj.key
        path = os.path.dirname(obj.key)
        make_dir = os.path.join(path)
        if not os.path.exists(path):
            try:
                os.makedirs(make_dir)
            except Exception as err:
                pass
        s3.Object(bucket_name, dest).download_file(dest)


bucket_name = 'kaotu'
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

download_all_file_in_folder(bucket_name)
