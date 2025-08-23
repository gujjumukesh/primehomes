import os
from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.files import File
from core.models import Project, Service, Logo, Slide, BackGroundImage

class Command(BaseCommand):
    help = 'Loads images from static/media directories into the database for various models.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting image population...")

        # Helper function to process a model and its image directory
        def populate_from_dir(model, dir_name, name_attr='name'):
            # Construct the full path to the source image directory
            source_dir = os.path.join(settings.BASE_DIR, 'static', 'media', dir_name)
            
            if not os.path.exists(source_dir):
                self.stdout.write(self.style.WARNING(f"Directory not found for {model.__name__}: {source_dir}. Skipping."))
                return

            self.stdout.write(f"--- Processing {model.__name__} from {source_dir} ---")
            
            # Clear existing data to avoid duplicates and stale entries
            model.objects.all().delete()
            self.stdout.write(f"Cleared all existing {model.__name__} objects.")

            # Iterate over files and create model instances
            for filename in os.listdir(source_dir):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    filepath = os.path.join(source_dir, filename)
                    instance_name = os.path.splitext(filename)[0]

                    try:
                        with open(filepath, 'rb') as f:
                            instance = model()
                            setattr(instance, name_attr, instance_name)
                            instance.image.save(filename, File(f), save=True)
                        self.stdout.write(self.style.SUCCESS(f"Created {model.__name__} '{instance_name}' with image '{filename}'"))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error creating {model.__name__} for {filename}: {e}"))

        populate_from_dir(Project, 'projects', 'title')
        populate_from_dir(Service, 'services', 'title')
        populate_from_dir(Logo, 'logo', 'name')
        populate_from_dir(Slide, 'sliding-images', 'title')
        populate_from_dir(BackGroundImage, 'bg-images', 'name')

        self.stdout.write(self.style.SUCCESS("Finished populating all images."))
