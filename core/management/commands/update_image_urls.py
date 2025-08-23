import os
from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import Service, Project
from core.supabase_utils import get_supabase_file_url
from dotenv import load_dotenv

load_dotenv()

class Command(BaseCommand):
    help = 'Update image URLs to point to Supabase storage'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be updated without making changes',
        )

    def handle(self, *args, **options):
        supabase_url = os.getenv("SUPABASE_URL")
        bucket_name = getattr(settings, 'SUPABASE_BUCKET_NAME', 'static-media')

        if not supabase_url:
            self.stdout.write(
                self.style.ERROR("SUPABASE_URL not found in .env file")
            )
            return

        self.stdout.write("🔄 Starting image URL update process...")
        
        # Update Service images
        self.stdout.write("\n📋 Updating Service image URLs...")
        services_updated = 0
        for service in Service.objects.all():
            if service.image:
                old_url = str(service.image)
                # Extract filename from the old URL
                filename = os.path.basename(old_url)
                new_url = get_supabase_file_url(filename, bucket_name)
                
                if options['dry_run']:
                    self.stdout.write(f"   Would update: {old_url} -> {new_url}")
                else:
                    service.image = new_url
                    service.save()
                    self.stdout.write(f"   ✅ Updated: {old_url} -> {new_url}")
                    services_updated += 1

        # Update Project images
        self.stdout.write("\n📋 Updating Project image URLs...")
        projects_updated = 0
        for project in Project.objects.all():
            if project.image:
                old_url = str(project.image)
                # Extract filename from the old URL
                filename = os.path.basename(old_url)
                new_url = get_supabase_file_url(filename, bucket_name)
                
                if options['dry_run']:
                    self.stdout.write(f"   Would update: {old_url} -> {new_url}")
                else:
                    project.image = new_url
                    project.save()
                    self.stdout.write(f"   ✅ Updated: {old_url} -> {new_url}")
                    projects_updated += 1

        if options['dry_run']:
            self.stdout.write(
                self.style.WARNING(
                    f"\n🔍 DRY RUN: Would update {services_updated} services and {projects_updated} projects"
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"\n✅ Successfully updated {services_updated} services and {projects_updated} projects"
                )
            )
            self.stdout.write("\n🎉 All image URLs have been updated to use Supabase storage!")
            self.stdout.write("\nNext steps:")
            self.stdout.write("1. Test your application locally")
            self.stdout.write("2. Deploy to Vercel: vercel --prod")
