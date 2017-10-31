# aws_draneops
AWS Tool For cross account scanning/reporting
- This tool I think is somewhere inbetween the current AWS CLI (2017) and the SDK.
- I see this being something for those needing a bit more than the AWS CLI while maybe not wanting to spend the time making it in the SDK.


## Future Plans:
- Add command line arguments to get details needed about the ec2 instances.
- Add more things to query for, than just EC2, like:
  - What EC2 instances have a route and have a security group permitting X


## The Setup:
- Install Python 2.7+
  - or spin up a docker instance w/ python
  - or intall git bash on windows
- Install boto:
`pip install boto3 --upgrade -y`


## Check Version:
- MacOS: pip freeze | grep boto3
- PC   : pip freeze | findstr boto3
- The version this worked for me on is: `boto3==1.4.7`


## Credentials
- Uses the AWS CLI credentials file, located in your home directory inside a folder named .aws.
  - script detects the OS and logged in user, to find the path of your .aws credentials file.
  - script then parses your .aws credentials file and scans all these accounts


## What's Next?
- Any feature requests would be awesome!
- I'd like to add some argument switches to make this a much more usable framework.
