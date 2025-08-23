import os
import supabase
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Supabase credentials from environment variables
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_KEY")

# Check if credentials are provided
if not supabase_url or not supabase_key:
    print("Error: SUPABASE_URL and SUPABASE_SERVICE_KEY must be set in the .env file.")
    exit()

# Initialize Supabase client
client = supabase.create_client(supabase_url, supabase_key)

# Function to upload files from a local directory to a Supabase bucket
def upload_directory_to_supabase(local_dir, bucket_name):
    if not os.path.isdir(local_dir):
        print(f"Error: Directory '{local_dir}' not found.")
        return

    # Create the bucket if it doesn't exist
    try:
        client.storage.get_bucket(bucket_name)
    except Exception:
        client.storage.create_bucket(bucket_name)

    for root, _, files in os.walk(local_dir):
        for file in files:
            local_path = os.path.join(root, file)
            # Create a relative path to maintain the directory structure in the bucket
            relative_path = os.path.relpath(local_path, local_dir).replace("\\", "/")
            supabase_path = f"{bucket_name}/{relative_path}"

            print(f"Uploading {local_path} to {supabase_path}...")

            with open(local_path, "rb") as f:
                try:
                    # Use the relative path as the file name in the bucket
                    client.storage.from_(bucket_name).upload(
                        path=relative_path,
                        file=f,
                        file_options={"content-type": "image/jpeg"}  # Adjust content type if needed
                    )
                    print(f"Successfully uploaded {file}")
                except Exception as e:
                    print(f"Error uploading {file}: {e}")

if __name__ == "__main__":
    # Specify the local directory and the Supabase bucket name
    static_media_directory = "static/media"
    bucket_name = "static-media"

    print(f"Starting upload from '{static_media_directory}' to bucket '{bucket_name}'...")
    upload_directory_to_supabase(static_media_directory, bucket_name)
    print("Upload process finished.")
