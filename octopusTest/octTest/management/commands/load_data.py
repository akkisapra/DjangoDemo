from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from adoptions.models import Pet, Vaccine
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

LOADED_ERROR_MESSAGE = """ If you need to reload the data from csv file, please delete the sqlite file 
and then run  'python manage.py migrate' to create new database with table"""
NEM13_FORMAT_ERROR_MESSAGE = "File received does not have NEM13 data"
class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from the csv"
    def handle(self,*args, **options):
        if bill.objects.exists():
            print("data already loaded.. exiting")
            print(LOADED_ERROR_MESSAGE)
            return
        print("loading data from the file")
        f=open("../../../AEMO556810778013NEM13.csv")
        fileData = f.readlines()
        if 'NEM13' not in fileData[0]:
            print("wrong file format.. exiting")
            print(NEM13_FORMAT_ERROR_MESSAGE)
            return

        for i in range(1,len(fileData)-1):



