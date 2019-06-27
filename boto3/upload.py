import boto3


BUCKET_NAME = 'kaotu'
path_local = './picupload/picture/yellow-octopus-funny-memes-68.jpg'
path_s3 = 'picupload/picture/yellow-octopus-funny-memes-68.jpg'

#s3.upload_file('FILE_NAME', 'BUCKET_NAME', 'OBJECT_NAME')
#FILE_NAME = path file or dir in localhost
#OBJECT_NAME = path file or create dir on s3

#s3 = boto3.client('s3')
#s3.upload_file(path_local, BUCKET_NAME, path_s3)

s3 = boto3.resource('s3')

#s3.meta.client.upload_file(path_local, BUCKET_NAME, path_s3)

#s3.Bucket(BUCKET_NAME).upload_file(path_local, path_s3)

s3.Object(BUCKET_NAME, path_s3).upload_file(path_local)
