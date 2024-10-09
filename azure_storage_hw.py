import os
from azure.storage.blob import BlobServiceClient

# Replace with your connection string and container name
connection_string = "BlobEndpoint=https://hha504demo.blob.core.windows.net/;QueueEndpoint=https://hha504demo.queue.core.windows.net/;FileEndpoint=https://hha504demo.file.core.windows.net/;TableEndpoint=https://hha504demo.table.core.windows.net/;SharedAccessSignature=sv=2022-11-02&ss=bfqt&srt=sco&sp=rwactfx&se=2025-10-10T02:50:46Z&st=2024-10-09T18:50:46Z&spr=https&sig=K0LdIws1fqaMrBuWzq2d6b%2Bp1BUAAJkOzkXlLp4cxjE%3D"
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
