from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Trip(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=4) # BD , Can, SWE
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    traveller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')

    def __str__(self):
        return f"{self.city}, {self.country} | {self.start_date.year}"


class Note(models.Model):
    EXCURSIONS = (
        ("Event", "event"),
        ("Food", "food"),
        ("General", "general"),
        ("Places", "places"),
    )
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=EXCURSIONS, default=(('general','General')))
    img = models.ImageField(upload_to='notes', null=True, blank=True)

    def __str__(self):
        return self.title

