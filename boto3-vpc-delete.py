import pprint
from boto3_helper import ec2_delete_vpc

result = ec2_delete_vpc('vpc-0c170b0963dd0d871')
pprint.pprint(result)