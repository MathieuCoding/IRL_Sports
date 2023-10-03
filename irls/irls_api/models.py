from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    last_name = models.CharField(max_length=200, blank=True, default='')
    first_name = models.CharField(max_length=200, blank=True, default='')
    email_address = models.EmailField(max_length=200, blank=True, default='')

    def __str__(self):
        return self.first_name
    
    class Meta:
        pass

class Structure(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')
    city = models.CharField(max_length=200, blank=True, default='')
    address = models.CharField(max_length=200, blank=True, default='')
    zip_code = models.IntegerField(blank=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        pass

class Sport(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return self.name
    
    class Meta:
        pass

class Event(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, default='')
    date = models.DateTimeField(blank=True, null=False)
    players_number = models.IntegerField(blank=True, null=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    sport = models.ForeignKey(Sport, on_delete = models.CASCADE, blank = True, null = True)
    structure = models.ForeignKey(Structure, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_date']