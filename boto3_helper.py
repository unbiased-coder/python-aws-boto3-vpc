import os
import boto3
import pprint
from dotenv import load_dotenv

def get_aws_keys():
    load_dotenv()
    return os.getenv('AWS_ACCESS_KEY'), os.getenv('AWS_SECRET_KEY')

def init_aws_session():
    access_key, secret_key = get_aws_keys()
    return boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=os.getenv('AWS_REGION'))

def ec2_get_vpc_list():
    session = init_aws_session()
    ec2 = session.client('ec2')
    response = ec2.describe_vpcs()
    return response['Vpcs']

def ec2_add_vpc(ip_block):
    session = init_aws_session()
    ec2 = session.client('ec2')
    response = ec2.create_vpc(CidrBlock = ip_block, InstanceTenancy='default')
    return response['Vpc']

def ec2_delete_vpc(vpc_id):
    session = init_aws_session()
    ec2 = session.client('ec2')
    response = ec2.delete_vpc(VpcId=vpc_id)
    return response
