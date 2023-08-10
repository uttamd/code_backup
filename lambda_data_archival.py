import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    try:
        source_bucket_name = 'sourcebucket0808'
        archival_bucket_name = 'archivebucket0808'
        current_date = datetime.utcnow()
        threshold_days = 0
        threshold_date = (current_date - timedelta(days=0)).strftime('%Y-%m-%d %H:%M:%S')
        s3_client = boto3.client('s3')
        
        # List objects in the source and archival buckets
        source_objects = s3_client.list_objects_v2(Bucket=source_bucket_name)
        archival_objects = s3_client.list_objects_v2(Bucket=archival_bucket_name)
        
        source_keys = [obj['Key'] for obj in source_objects.get('Contents', [])]
        archival_keys = [obj['Key'] for obj in archival_objects.get('Contents', [])]
        
        for key in source_keys:
            if key not in archival_keys:
                destination_key = key
                print(f"Copying file '{key}' to archival bucket.")
                copy_source = {'Bucket': source_bucket_name, 'Key': key}
                s3_client.copy_object(CopySource=copy_source, Bucket=archival_bucket_name, Key=destination_key)
        
        # file deletion if exceeds to threshold 
        if 'Contents' in archival_objects:
            for file in archival_objects['Contents']:
                key = file['Key']
                last_modified = file['LastModified'].strftime('%Y-%m-%d %H:%M:%S')
                print('last_modified date ',last_modified)
                print('threshold_date ',threshold_date)
                
                # Check if the object is older than the threshold date
                if last_modified < threshold_date:
                    print(f"Deleting file '{key}'")
                    s3_client.delete_object(Bucket=archival_bucket_name, Key=key)
        return {
            'statusCode': 200,
            'body': 'Archival process completed.'
        }
    except Exception as e:
        print("excpetion occured !",e)