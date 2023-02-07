from django.db import models



from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField


MY_CHOICES = (('Telugu', 'Telugu'),
           ('Hindhi', 'Hindhi'),
           ('English', 'English'),
           ('Mathematics', 'Mathematics'),
           ('Social', 'Social'),
           ('Science', 'Science'))
# Create your models here.
class TeachersData(models.Model):
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100)
    # profile_picture = models.CharField(max_length=100)
    profile_picture = models.ImageField()
    email_address = models.EmailField(max_length = 254)
    phone_number = models.CharField(max_length=1000)
    room_number = models.CharField(max_length=100)
    subjects_taught = MultiSelectField(choices=MY_CHOICES, max_choices=5)
    class Meta:
        db_table = "teachers_data"
        