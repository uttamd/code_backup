import subprocess
import os
from datetime import datetime,timedelta

print(f"current directory-> {os.getcwd()}")

def incremental_backup(source, destination):
    # Generate a timestamp for the backup
    backup_timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Construct the rsync command for incremental backup
    rsync_command = [
        'rsync', '-a', '--delete', '--link-dest=' + destination , source + '/', destination
    ]
    
    # Execute the rsync command
    try:
        subprocess.run(rsync_command, check=True)
        print("Incremental backup completed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error during backup:", e)
    except Exception as e :
      print("exception occured in incremental_backup function",e)

def file_deletion(source_directory):
  try:
      current_date = datetime.utcnow()
      threshold_days = 0
      threshold_date = (current_date - timedelta(days=threshold_days)).strftime('%Y%m%d%H%M')
      for root, dirs, files in os.walk(source_directory):
          for file in files:
              file_path = source_directory+'/'+ file
              file_modified_dt = time.strftime('%Y%m%d%H%M', time.gmtime(os.path.getmtime(file_path)))
              if file_modified_dt < threshold_date :
                print(f"file applicable for deletion-> , {file_path} , modified_date {file_modified_dt}--threshold_date --{threshold_date}")
                os.remove(file_path)
                print(f'{file_path} deleted successfully')
  except Exception as e:
    print("exception occured in file_deletion function !",e)

if __name__ == '__main__':
    source_directory = 'drive/MyDrive/source_loc'
    destination_directory = 'drive/MyDrive/dest_loc'
    incremental_backup(source_directory, destination_directory)
    file_deletion(destination_directory)
