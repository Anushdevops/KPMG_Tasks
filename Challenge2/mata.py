import boto3
import json

def get_instance_metadata(data_key=None):
    client = boto3.client('ec2')
    response = client.describe_instances()
    instances = response['Reservations'][0]['Instances']
    instance_metadata = {}
    for instance in instances:
        instance_id = instance['InstanceId']
        instance_metadata[instance_id] = {}
        for key, value in instance.items():
            if data_key is None or key == data_key:
                instance_metadata[instance_id][key] = value
    return json.dumps(instance_metadata, indent=4)
    
 print(get_instance_metadata())