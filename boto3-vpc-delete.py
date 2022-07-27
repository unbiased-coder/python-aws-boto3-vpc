import pprint
from boto3_helper import ec2_delete_vpc

result = ec2_delete_vpc('vpc-0c5659f4344044b0a')
pprint.pprint(result)