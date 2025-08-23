#!/usr/bin/env python3
"""
Quick setup script for Supabase integration
This script helps you test your Supabase connection and create the storage bucket.
"""

import os
import sys
from dotenv import load_dotenv

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Load environment variables
load_dotenv()

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'construction_company.settings')

# Configure Django
import django
django.setup()

def main():
    print("🔧 Supabase Setup Helper")
    print("=" * 40)
    
    # Check environment variables
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_KEY")
    
    if not supabase_url or not supabase_key:
        print("❌ Missing Supabase credentials in .env file")
        print("\nPlease create a .env file with:")
        print("SUPABASE_URL=https://your-project-id.supabase.co")
        print("SUPABASE_SERVICE_KEY=your_service_role_key_here")
        return
    
    print("✅ Environment variables found")
    print(f"   URL: {supabase_url}")
    print(f"   Key: {supabase_key[:20]}...")
    
    # Test Supabase connection
    try:
        from core.supabase_utils import get_supabase_client
        client = get_supabase_client()
        
        if client:
            print("✅ Supabase connection successful!")
            
            # Try to create the bucket
            bucket_name = "static-media"
            try:
                client.storage.create_bucket(bucket_name, public=True)
                print(f"✅ Created storage bucket: {bucket_name}")
            except Exception as e:
                if "already exists" in str(e).lower():
                    print(f"✅ Storage bucket '{bucket_name}' already exists")
                else:
                    print(f"⚠️  Could not create bucket: {e}")
            
            print("\n🎉 Setup completed successfully!")
            print("\nNext steps:")
            print("1. Run: python upload_to_supabase.py")
            print("2. Run: python manage.py update_image_urls")
            print("3. Deploy: python deploy_to_vercel.py")
            
        else:
            print("❌ Could not create Supabase client")
            
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure you're running this from the project root directory")
    except Exception as e:
        print(f"❌ Connection error: {e}")
        print("Please check your Supabase credentials and project status")

if __name__ == "__main__":
    main() 