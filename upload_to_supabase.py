import os
import sys
from dotenv import load_dotenv

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Load environment variables from .env file
load_dotenv()

# Import Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_company.settings')
import django
django.setup()

from core.supabase_utils import upload_directory_to_supabase, get_supabase_client

def main():
    # Get Supabase credentials from environment variables
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_KEY")

    # Check if credentials are provided
    if not supabase_url or not supabase_key:
        print("Error: SUPABASE_URL and SUPABASE_SERVICE_KEY must be set in the .env file.")
        print("Please create a .env file with your Supabase credentials.")
        return

    # Test Supabase connection
    client = get_supabase_client()
    if not client:
        print("Error: Could not create Supabase client.")
        return

    print("✅ Supabase connection successful!")

    # Define directories to upload
    directories_to_upload = [
        ("static/media", "static-media"),
        ("staticfiles/media", "static-media"),
    ]

    for local_dir, bucket_name in directories_to_upload:
        if os.path.exists(local_dir):
            print(f"\n📁 Uploading directory: {local_dir}")
            print(f"🪣 Bucket: {bucket_name}")
            
            try:
                uploaded_files = upload_directory_to_supabase(local_dir, bucket_name)
                print(f"✅ Successfully uploaded {len(uploaded_files)} files from {local_dir}")
                
                # Print uploaded files
                for file_path in uploaded_files:
                    supabase_url = get_supabase_file_url(file_path, bucket_name)
                    print(f"   📄 {file_path} -> {supabase_url}")
                    
            except Exception as e:
                print(f"❌ Error uploading {local_dir}: {e}")
        else:
            print(f"⚠️  Directory not found: {local_dir}")

    print("\n🎉 Upload process completed!")
    print("\nNext steps:")
    print("1. Run: python manage.py update_image_urls")
    print("2. Deploy to Vercel: vercel --prod")

def get_supabase_file_url(file_path, bucket_name):
    """Get the public URL for a file in Supabase storage"""
    supabase_url = os.getenv("SUPABASE_URL")
    if not supabase_url:
        return None
    
    return f"{supabase_url}/storage/v1/object/public/{bucket_name}/{file_path}"

if __name__ == "__main__":
    main()
