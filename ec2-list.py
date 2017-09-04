#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Docstring
"""

__author__ = "Joseph Drane"
__version__ = "0.1.0"
__license__ = "MIT"

# MacOS: pip freeze | grep boto3
# PC   : pip freeze | findstr boto3
# boto3==1.4.7
import boto3
import csv


# Find all EC2 instances in all regions for a single account.
def get_ec2(account_profile):
    session = boto3.Session(profile_name=account_profile)
    client = session.client('ec2',region_name='us-east-1')
    ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    for region in ec2_regions:
        ec2 = session.resource('ec2', region_name=region)
        instances = ec2.instances.filter()
        with open('EC2_In_All_Accounts.csv', 'ab') as myfile:
            wr = csv.writer(myfile, dialect='excel')
            for instance in instances:
                try:
                    for tag in instance.tags:
                        if tag['Key'] == 'Name':
                            instancename = tag['Value']
                except:
                    instancename = 'Has No Name'
                # mylist = [instancename, instance.id, instance.instance_type, region]
                mylist = [instancename, instance.private_ip_address, instance.state['Name']]
                print mylist
                wr.writerow(mylist)
        myfile.close

# Runs get_ec2 for each profile
def main():
    """ Main entry point of the app """
    aws_cli_profiles = ['Prod','SandBox','security','Non-Prod']
    for profile in aws_cli_profiles:
        try:
            get_ec2(profile)
        except:
            print "The %s profile didn't work." % profile


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
