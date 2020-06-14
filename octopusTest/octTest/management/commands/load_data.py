from datetime import datetime
import os
from django.core.management import BaseCommand
from octTest.models import bill
from pytz import UTC


DATETIME_FORMAT = '%Y%m%d%H%M%S'

LOADED_ERROR_MESSAGE = """ If you need to reload the data from csv file, please delete the sqlite file 
and then run  'python manage.py migrate' to create new database with table"""
NEM13_FORMAT_ERROR_MESSAGE = "File received does not have NEM13 data"
FILES_PATH='../../../files'
class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from the csv"
    def handle(self,*args, **options):
        if bill.objects.exists():
            print("data already loaded.. exiting")
            print(LOADED_ERROR_MESSAGE)
            return
        print("loading data from the file")
        if not os.listdir(FILES_PATH):
            print("Files not found !!")
        else:
            file_names = os.listdir(FILES_PATH)
        for each in file_names:
            f=open(str(FILES_PATH+each))
            file_data = f.readlines()
            if 'NEM13' not in file_data[0]:
                print("wrong file format.. exiting")
                print(NEM13_FORMAT_ERROR_MESSAGE)
                break
            for i in range(1, len(file_data) - 1):
                fileDataEach = file_data[i].split(",")
                billObj = bill()
                billObj.NMI = fileDataEach[1]
                billObj.serial = fileDataEach[6]
                billObj.readingValue = fileDataEach[13]
                billObj.fileName = each
                raw_submission_date = fileDataEach[14]
                submission_date = UTC.localize(datetime.strptime(raw_submission_date, DATETIME_FORMAT))
                billObj.date = submission_date
                billObj.save()




