import pprint
from boto3_helper import ec2_get_vpc_list

result = ec2_get_vpc_list()
pprint.pprint(result)