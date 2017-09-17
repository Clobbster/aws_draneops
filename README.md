# aws_draneops
AWS Tool For cross account scanning/reporting
- still building this app. just saving here to not lose work.


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
- The profile names in here must be in the script inside the main function.


## Help Section
- coming soon...
