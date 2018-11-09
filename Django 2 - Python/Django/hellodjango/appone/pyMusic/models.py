from django.db import models


class Song(models.Model):
    album = models.ForeignKey('Album',
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    duration = models.IntegerField(default=0, help_text="Duration in seconds")
    lyrics = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey('artist', on_delete=models.CASCADE)
    release_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.artist)


class Artist(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    join_date = models.DateField(
        help_text="Date when the artist joined the PyPyMusic")
    published = models.BooleanField(default=False)
    biography = models.TextField(blank=True)

    def full_name(self):
        if not self.first_name:
            return self.last_name
        else:
            return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name()
