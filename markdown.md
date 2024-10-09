## 1 - Screenshots of the file upload process in Azure Blob Storage and GCP Cloud Storage using the GUI
### **Azure**
<<<<<<< HEAD
### Create a new Storage Account
<img width="1470" alt="Screenshot 2024-10-09 at 14 14 19" src="https://github.com/user-attachments/assets/48383007-ea89-41e2-92d9-bad8be9d4745">

### Find the Upload button and create a new container
<img width="586" alt="Screenshot 2024-10-09 at 14 15 31" src="https://github.com/user-attachments/assets/a4986696-28b8-43b4-9343-8e0b88d5e8e5">

### Navigate to the Containers tab and click on the one you just created
<img width="1470" alt="Screenshot 2024-10-09 at 14 18 24" src="https://github.com/user-attachments/assets/a53453ba-7f7e-4c96-ae74-c3cd9d994b45">

### View your images!
<img width="1186" alt="Screenshot 2024-10-09 at 14 18 33" src="https://github.com/user-attachments/assets/e933e607-f003-4c60-9aaf-5564c7ceed04">
=======


>>>>>>> d50b5bf (Initial commit)

### **GCP**
### Navigate to Cloud Storage>Buckets
<img width="1470" alt="Screenshot 2024-10-09 at 10 31 34" src="https://github.com/user-attachments/assets/cd03d6ad-97ac-478f-ac02-5df655f9cb67">

 
### In the Objects tab, click the Upload Files button
<img width="641" alt="Screenshot 2024-10-09 at 10 32 29" src="https://github.com/user-attachments/assets/460ba806-2acc-4ff0-a29e-da2034822296">


### Your images are uploaded! Click on them for more details
<img width="1202" alt="Screenshot 2024-10-09 at 10 33 12" src="https://github.com/user-attachments/assets/bf15df28-f669-4505-9d3d-8a1b14710861">


## 2 - Python code for uploading files to Azure Blob Storage and GCP Cloud Storage
### **Azure**
<<<<<<< HEAD
    import os
    from azure.storage.blob import BlobServiceClient

    # Replace with your connection string and container name
    connection_string = 
    "BlobEndpoint=https://hha504demo.blob.core.windows.net/;QueueEndpoint=https://hha504demo.queue.core.windows.net/;FileEndpoint=https://hha504demo.file.core.windows.net/;TableEndpoint=https://hha504demo.table.core.windows.net/;SharedAccessSignature=sv=2022-11-02&ss=bfqt&srt=sco&sp=rwactfx&se=2025-10-10T02:50:46Z&st=2024-10-09T18:50:46Z&spr=https&sig=K0LdIws1fqaMrBuWzq2d6b%2Bp1BUAAJkOzkXlLp4cxjE%3D"
    container_name = "hha504-demo"
    local_folder = "/Users/janna/hha-projects/HHA504_assignment_storage/images2"

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Create the container if it does not exist
    container_client = blob_service_client.get_container_client(container_name)
    try:
        container_client.create_container()
    except Exception as e:
        print(f"Container already exists: {e}")

    # Function to upload files
    def upload_files_from_folder(local_folder):
        for filename in os.listdir(local_folder):
            local_file_path = os.path.join(local_folder, filename)

            if os.path.isfile(local_file_path):
                blob_client = container_client.get_blob_client(filename)
                with open(local_file_path, "rb") as data:
                    blob_client.upload_blob(data, overwrite=True)
                print(f"Uploaded: {filename}")

    # Upload images
    upload_files_from_folder(local_folder)


### **GCP**
    from google.cloud import storage
    from PIL import Image
    import io
    import os

    # Step 1: Set up your Google credentials
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcp_key.json'

    # Step 2: Create a Google Cloud Storage client
    client = storage.Client()

    # Step 3: Create a bucket or use an existing one
    bucket_name = 'jan-504-demo'  
    bucket = client.bucket(bucket_name)

    files_upload = []
     for root, dirs, files in os.walk("images"):
        for file in files:
            files_upload.append(os.path.join(root,file))

    for file in files_upload:
        print(f"Working on {file}")

        with open(file, 'rb') as f:
            file_byte_array = f.read()
        print(file)

    try:
        blob = bucket.blob(file)
        blob.upload_from_string(file_byte_array, content_type='image/png')   
        print("Image uploaded successfully to Google Cloud Storage!")
    except Exception as e:
        print(f"Error: {e}")

=======
    this is code


### **GCP**
    this is code
>>>>>>> d50b5bf (Initial commit)

## 3 - Notes on storage management and security features in Azure and GCP
### **Azure**


### **GCP**
<<<<<<< HEAD
To manage and secure data in Google Cloud Storage (GCS), utilize IAM for access control through roles and service accounts, and consider ACLs for granular permissions. Implement server-side encryption for data at rest, and use lifecycle rules to optimize storage costs by automatically transitioning or deleting objects. Monitor access with Cloud Audit Logs and employ VPC Service Controls for network security. Additionally, enable versioning and retention policies to safeguard data against accidental deletions, and regularly review permissions to adhere to the principle of least privilege. Combining these strategies ensures a secure and efficient data management approach in GCS.
=======
>>>>>>> d50b5bf (Initial commit)
