import os
from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import Service, Project
from dotenv import load_dotenv

load_dotenv()

class Command(BaseCommand):
    help = 'Update image URLs to point to Supabase storage'

    def handle(self, *args, **options):
        supabase_url = os.getenv("SUPABASE_URL")
        bucket_name = "static-media"

        if not supabase_url:
            self.stdout.write(self.style.ERROR("SUPABASE_URL not found in .env file"))
            return

        self.stdout.write("Updating image URLs...")
        for model in [Service, Project]:
            self.stdout.write(f"Updating {model.__name__} image URLs...")
            for item in model.objects.all():
                try:
                    if item.image:
                        image_path = str(item.image)
                        item.image = f"{supabase_url}/storage/v1/object/public/{bucket_name}/{image_path}"
                        item.save()
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error updating {model.__name__} {item.id}: {e}"))
            self.stdout.write(self.style.SUCCESS(f"{model.__name__} image URLs updated."))
