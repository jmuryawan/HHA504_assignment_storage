from google.cloud import storage
from PIL import Image
import io
import os

# Step 1: Set up your Google credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcp_key.json'

# Step 2: Create a Google Cloud Storage client
client = storage.Client()

# Step 3: Create a bucket or use an existing one
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
