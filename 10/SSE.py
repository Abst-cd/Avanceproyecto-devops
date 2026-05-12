                                                                                                                                                    SSE.py                                                                                                                                                                   
import boto3

s3_client = boto3.client('s3')
bucket_name = "solucionestechbucket"

def set_bucket_encryption(bucket):
    try:
        s3_client.put_bucket_encryption(
            Bucket=bucket,
            ServerSideEncryptionConfiguration={
                'Rules': [{
                    'ApplyServerSideEncryptionByDefault': {
                        'SSEAlgorithm': 'AES256'
                    }
                }]
            }
        )
        print(f"Cifrado AES256 habilitado para: {bucket}")
    except Exception as e:
        print(f"Error al configurar cifrado: {e}")

set_bucket_encryption(bucket_name)
