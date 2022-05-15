from django.db import models

from django.db import models

class State(models.Model):
    stateName = models.CharField(max_length=100)

    def __str__(self):
        return self.stateName

class Shelter(models.Model):
    state = models.ForeignKey(State, 
    on_delete=models.CASCADE, 
    related_name='shelters')
    shelterName = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.shelterName

class Canine(models.Model):
    shelter = models.ForeignKey(Shelter, 
    on_delete=models.CASCADE, 
    related_name='canines', 
    null=True)
    dogName = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    photo_url = models.CharField(max_length=400, default = "no dice!")

    def __str__(self):
        return self.dogName

class Feline(models.Model):
    shelter = models.ForeignKey(Shelter, 
    on_delete=models.CASCADE, 
    related_name='felines', 
    null=True)
    catName = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    photo_url = models.CharField(max_length=400, default = "no dice!")

    def __str__(self):
        return self.catName
