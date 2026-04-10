import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

for reserva in response['Reservations']:
    for instancia in reserva['Instances']:
        print("ID:", instancia['InstanceId'])
        print("Estado:", instancia['State']['Name'])
        print("Tipo:", instancia['InstanceType'])
        print("-----")