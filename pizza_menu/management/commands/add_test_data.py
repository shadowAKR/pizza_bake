import os, shutil
from django.core.management.base import BaseCommand
from django.conf import settings

from pizza_menu.models import Pizza
from pizza_menu.test_data import pizza_list

class Command(BaseCommand):
    '''Action Bulk create'''
    help = "Action Data Import"
    def handle(self, *args, **options):
        try:
            for data in pizza_list:
                obj = Pizza(**data)
                obj.save()
            files = os.listdir(os.path.join(settings.BASE_DIR, "pizza_menu/data/"))
            os.makedirs(settings.MEDIA_ROOT + "/pizzas", exist_ok=True)
            # Copy each file to the destination folder
            for file in files:
                source_file = os.path.join("pizza_menu/data/", file)
                destination_file = os.path.join(settings.MEDIA_ROOT + "/pizzas/", file)
                shutil.copy2(source_file, destination_file)  # shutil.copy2() preserves metadata
            return "success"
        except Exception:
            return "failed"