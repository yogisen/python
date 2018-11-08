from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField(default=0, help_text="Duration in seconds")
    lyrics = models.TextField(blank=True)

    def __str__(self):
        return self.name
