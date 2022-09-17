from django.db import models

class Passenger(models.Model):
    firstName = models.CharField( primary_key=True, max_length= 20)
    lastName = models.CharField( max_length= 20)
    travelPoints = models.CharField( max_length= 20)


