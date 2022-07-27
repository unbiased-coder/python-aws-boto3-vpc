import pprint
from boto3_helper import ec2_add_vpc

result = ec2_add_vpc('172.31.0.0/16')
pprint.pprint(result)