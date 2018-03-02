from django.core.management.base import BaseCommand
from website.models import SocialData
import facebook, datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        print 0