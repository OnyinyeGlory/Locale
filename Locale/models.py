import uuid

from django.db import models


class Region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)


class State(models.Model):
    id = models.CharField(primary_key=True, max_length=3)
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    slogan = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class LGA(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="lgas")

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities")

    def __str__(self):
        return self.name
