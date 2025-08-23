import os
import supabase
from django.conf import settings
from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from urllib.parse import urljoin

class SupabaseStorage(Storage):
    """
    Custom storage backend for Supabase
    """
    
    def __init__(self, bucket_name=None):
        self.bucket_name = bucket_name or getattr(settings, 'SUPABASE_BUCKET_NAME', 'static-media')
        self.supabase_url = getattr(settings, 'SUPABASE_URL', None)
        self.supabase_key = getattr(settings, 'SUPABASE_SERVICE_KEY', None)
        
        if self.supabase_url and self.supabase_key:
            self.client = supabase.create_client(self.supabase_url, self.supabase_key)
        else:
            self.client = None
    
    def _open(self, name, mode='rb'):
        if not self.client:
            raise Exception("Supabase client not configured")
        
        try:
            response = self.client.storage.from_(self.bucket_name).download(name)
            return ContentFile(response)
        except Exception as e:
            raise Exception(f"Error opening file {name}: {e}")
    
    def _save(self, name, content):
        if not self.client:
            raise Exception("Supabase client not configured")
        
        try:
            self.client.storage.from_(self.bucket_name).upload(
                path=name,
                file=content,
                file_options={"content-type": content.content_type}
            )
            return name
        except Exception as e:
            raise Exception(f"Error saving file {name}: {e}")
    
    def exists(self, name):
        if not self.client:
            return False
        
        try:
            self.client.storage.from_(self.bucket_name).list(path=os.path.dirname(name))
            return True
        except:
            return False
    
    def url(self, name):
        """Return the public URL for the file"""
        if not self.supabase_url:
            return None
        
        return f"{self.supabase_url}/storage/v1/object/public/{self.bucket_name}/{name}"
    
    def delete(self, name):
        if not self.client:
            return
        
        try:
            self.client.storage.from_(self.bucket_name).remove([name])
        except Exception as e:
            print(f"Error deleting file {name}: {e}")

def get_supabase_client():
    """Get a Supabase client instance"""
    supabase_url = getattr(settings, 'SUPABASE_URL', None)
    supabase_key = getattr(settings, 'SUPABASE_SERVICE_KEY', None)
    
    if not supabase_url or not supabase_key:
        return None
    
    return supabase.create_client(supabase_url, supabase_key)

def upload_file_to_supabase(file_path, bucket_name=None, remote_path=None):
    """Upload a single file to Supabase storage"""
    client = get_supabase_client()
    if not client:
        raise Exception("Supabase client not configured")
    
    bucket_name = bucket_name or getattr(settings, 'SUPABASE_BUCKET_NAME', 'static-media')
    
    if not remote_path:
        remote_path = os.path.basename(file_path)
    
    try:
        with open(file_path, 'rb') as f:
            client.storage.from_(bucket_name).upload(
                path=remote_path,
                file=f,
                file_options={"content-type": "image/jpeg"}
            )
        return f"{getattr(settings, 'SUPABASE_URL')}/storage/v1/object/public/{bucket_name}/{remote_path}"
    except Exception as e:
        raise Exception(f"Error uploading file {file_path}: {e}")

def upload_directory_to_supabase(local_dir, bucket_name=None):
    """Upload all files from a directory to Supabase storage"""
    client = get_supabase_client()
    if not client:
        raise Exception("Supabase client not configured")
    
    bucket_name = bucket_name or getattr(settings, 'SUPABASE_BUCKET_NAME', 'static-media')
    
    # Create bucket if it doesn't exist
    try:
        client.storage.get_bucket(bucket_name)
    except:
        client.storage.create_bucket(bucket_name)
    
    uploaded_files = []
    
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local_dir).replace("\\", "/")
            
            try:
                with open(local_path, 'rb') as f:
                    client.storage.from_(bucket_name).upload(
                        path=relative_path,
                        file=f,
                        file_options={"content-type": "image/jpeg"}
                    )
                uploaded_files.append(relative_path)
                print(f"Uploaded: {relative_path}")
            except Exception as e:
                print(f"Error uploading {relative_path}: {e}")
    
    return uploaded_files

def get_supabase_file_url(file_path, bucket_name=None):
    """Get the public URL for a file in Supabase storage"""
    supabase_url = getattr(settings, 'SUPABASE_URL', None)
    if not supabase_url:
        return None
    
    bucket_name = bucket_name or getattr(settings, 'SUPABASE_BUCKET_NAME', 'static-media')
    return f"{supabase_url}/storage/v1/object/public/{bucket_name}/{file_path}" 