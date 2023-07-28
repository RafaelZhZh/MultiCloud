
import boto3,sys

access_key = sys.argv[1]
secret_key = sys.argv[2]
region = sys.argv[3]
ami = sys.argv[4]
instance_type = sys.argv[5]

session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
)

ec2 = session.resource('ec2', region_name=region)

instances = ec2.create_instances(
    ImageId=ami,
    MinCount=1,
    MaxCount=1,
    InstanceType=instance_type
)

# Imprime el resultado de la operación
print("Instancia creada:", instances)