from django.db import models

# Create your models here.


class RoomMember(models.Model):
    name=models.CharField(max_length=200)
    uid=models.CharField(max_length=200)
    room_name=models.CharField(max_length=200)

    def __str__(self):
        return self.name



"""
    Create database model (RoomMember)--> Store user name, uid and room name
    1) On Join event, create (RoomMember) database
    2) On handleUserJoin event, query db for room member name by uid
    3) On leave event, delete (RoomMember)
""" 

