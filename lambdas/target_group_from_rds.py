import os
import sys
import json
import logging
import boto3

sys.path.append(f"{os.environ['LAMBDA_TASK_ROOT']}/lib")
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import cfnresponse
          
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('got event {}'.format(event))  
    try: 
        responseData = {}
        if event['RequestType'] == 'Delete':
            logger.info('Incoming RequestType: Delete operation') 
            cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
        if event['RequestType'] in ["Create", "Update"]:                      
            # 1. retrieve resource reference ID or Name
            ResourceRef=event['ResourceProperties']['ResourceRef']
            # 2. retrieve boto3 client    
            # client = boto3.client('ec2')
            # 3. Invoke describe/retrieve function using ResourceRef
            # response = client.describe_security_groups(GroupIds=[ResourceRef])
            # 4. Parse and return required attributes 
            responseData = {}
            responseData['SecurityGroup-Name']= 'TODO'
            logger.info('Retrieved SecurityGroup-Name!')
            cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)
        else:
            logger.info('Unexpected RequestType!') 
            cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)
    except Exception as err:
        logger.error(err)
        responseData = {"Data": str(err)}
        cfnresponse.send(event,context,cfnresponse.FAILED,responseData)
    return              