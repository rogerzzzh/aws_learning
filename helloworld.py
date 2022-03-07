import boto3
import io

s3 = boto3.resource("s3")

# list all buckets
for bucket in s3.buckets.all():
    print("There's a bucket called", bucket.name)

# update an object to bucket as stream
data = open("data/test_data.csv", "rb")
s3.Bucket("yzawsbucket").put_object(Key='test_data.csv', Body=data)

# stream an object from bucket
retrived_data = io.BytesIO()
s3.Object("yzawsbucket", "test_data.csv").download_fileobj(retrived_data)
print("Data is:", retrived_data.getvalue().decode("utf-8"))