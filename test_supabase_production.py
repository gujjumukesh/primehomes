#!/usr/bin/env python3
"""
Test script to verify Supabase integration is working
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

from core.models import Service, Project
from core.supabase_utils import get_supabase_file_url

def main():
    print("🔍 Supabase Integration Test")
    print("=" * 40)
    
    # Test 1: Check environment variables
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_KEY")
    
    print(f"✅ SUPABASE_URL: {supabase_url}")
    print(f"✅ SUPABASE_KEY: {supabase_key[:20]}..." if supabase_key else "❌ Missing")
    
    # Test 2: Check Supabase client
    try:
        from core.supabase_utils import get_supabase_client
        client = get_supabase_client()
        if client:
            print("✅ Supabase client created successfully")
        else:
            print("❌ Could not create Supabase client")
    except Exception as e:
        print(f"❌ Error creating Supabase client: {e}")
    
    # Test 3: Check current image URLs in database
    print("\n📋 Current Image URLs in Database:")
    
    print("\n🏗️  Projects:")
    projects = Project.objects.all()
    for project in projects:
        if project.image:
            print(f"   📄 {project.title}: {project.image}")
            # Check if it's a Supabase URL
            if 'supabase.co' in str(project.image):
                print(f"      ✅ Supabase URL detected")
            else:
                print(f"      ⚠️  Not a Supabase URL")
        else:
            print(f"   📄 {project.title}: No image")
    
    print("\n🔧 Services:")
    services = Service.objects.all()
    for service in services:
        if service.image:
            print(f"   📄 {service.title}: {service.image}")
            if 'supabase.co' in str(service.image):
                print(f"      ✅ Supabase URL detected")
            else:
                print(f"      ⚠️  Not a Supabase URL")
        else:
            print(f"   📄 {service.title}: No image")
    
    # Test 4: Test Supabase file URL generation
    print("\n🔗 Testing Supabase URL Generation:")
    test_file = "test-image.jpg"
    supabase_url = get_supabase_file_url(test_file)
    print(f"   Test file '{test_file}' -> {supabase_url}")
    
    print("\n🎉 Test completed!")

if __name__ == "__main__":
    main() 