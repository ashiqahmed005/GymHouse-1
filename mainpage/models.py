from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

BEGINNER = '1'
INTERMEDIATE = '2'
ADVANCED = '3'
EXPERT = '4'

LEVEL_TYPE_CHOICES = (
    (BEGINNER, 'Beginner'),
    (INTERMEDIATE, 'Intermediate'),
    (ADVANCED, 'Advanced'),
    (EXPERT, 'Expert'),
)

REGULAR = 'REG'
TRAINER = 'TRN'
ADMIN = 'ADM'

STATUS_CHOICES = (
    (REGULAR, 'Regular'),
    (TRAINER, 'Trainer'),
    (ADMIN, 'Admin'),
)

"""
class Level(models.Model):
    

    training_level = models.CharField(
        max_length=1,
        choices = LEVEL_TYPE_CHOICES,
        default = BEGINNER,
    )

    def is_beginner(self):
        return self.training_level == BEGINNER

    

class UserStatus(models.Model):
    

    status = models.CharField(
        max_length = 3,
        choices = STATUS_CHOICES,
        default = REGULAR,
    )


    def is_regular(self):
        return self.status == REGULAR

"""
#EXTENDS THE DEFAULT DJANGO USER
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #status = models.ForeignKey(UserStatus, related_name='User_status')
    status = models.CharField(max_length = 3, choices = STATUS_CHOICES, default = REGULAR)
    #level = models.ForeignKey(Level, related_name='Training_level_of_user')
    level = models.CharField(max_length=1, choices = LEVEL_TYPE_CHOICES, default = BEGINNER)


    first_name = models.CharField(max_length=15, default='NOFNAME')
    last_name = models.CharField(max_length=20, default='NOFNAME')

    age = models.IntegerField(blank=True, null=True, help_text='Please enter age')
    height = models.IntegerField(blank=True, null=True, help_text='Please enter height in cm.')
    weight = models.IntegerField(blank=True, null=True, help_text='Please enter weight in kg')

    def __unicode__(self):
        return self.first_name


class Event(models.Model):
    #event_id = models.IntegerField()
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    date = models.DateField()
    date_created = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Profile, related_name='Creator_of_event', blank=True, null=True)
    participants = models.ManyToManyField(Profile, related_name='Participants_of_event', blank=True) #No user yet, so ''
    trainer = models.ForeignKey(Profile, related_name='Trainer_of_event')
    # level = models.ForeignKey(Level, related_name='Training_level_of_event')
    level = models.CharField(max_length=1, choices = LEVEL_TYPE_CHOICES, default = BEGINNER)
    #def __str__(self): # __unicode__ on Python 2?
        #return ' '.join([self.ID, self.name, self.date])

    def __unicode__(self):
        return self.name
