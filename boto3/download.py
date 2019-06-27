import boto3


BUCKET_NAME = 'kaotu'
path_local = './picdownload/picture/downloadmeme.jpg'
path_s3 = 'picupload/picture/yellow-octopus-funny-memes-68.jpg'

s3 = boto3.client('s3')
s3.download_file(BUCKET_NAME, path_s3, path_local)

#s3 = boto3.resource('s3')

#s3.meta.client.download_file(BUCKET_NAME, path_s3, path_local)

#s3.Bucket(BUCKET_NAME).download_file(path_s3, path_local)

#s3.Object(BUCKET_NAME, path_s3).download_file(path_local)


