## 1 - Screenshots of the file upload process in Azure Blob Storage and GCP Cloud Storage using the GUI
### **Azure**



### **GCP**
### Navigate to Cloud Storage>Buckets
<img width="1470" alt="Screenshot 2024-10-09 at 10 31 34" src="https://github.com/user-attachments/assets/cd03d6ad-97ac-478f-ac02-5df655f9cb67">

 
### In the Objects tab, click the Upload Files button
<img width="641" alt="Screenshot 2024-10-09 at 10 32 29" src="https://github.com/user-attachments/assets/460ba806-2acc-4ff0-a29e-da2034822296">


### Your images are uploaded! Click on them for more details
<img width="1202" alt="Screenshot 2024-10-09 at 10 33 12" src="https://github.com/user-attachments/assets/bf15df28-f669-4505-9d3d-8a1b14710861">


## 2 - Python code for uploading files to Azure Blob Storage and GCP Cloud Storage
### **Azure**
    this is code


### **GCP**
    from google.cloud import storage
    from PIL import Image
    import io
    import os

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcp_key.json'

     client = storage.Client()

     bucket_name = 'jan-504-demo'  # Change this to your bucket name
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

## 3 - Notes on storage management and security features in Azure and GCP
### **Azure**


### **GCP**
