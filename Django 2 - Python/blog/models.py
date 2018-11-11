from django.db import models
from django.template.defaultfilters import slugify


class PostCategory(models.Model):
    name = models.CharField(max_length=50)

    def slug(self):
        return slugify(self.name)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('PostCategory',
                                 null=True,
                                 blank=True,
                                 on_delete=models.DO_NOTHING)
    published = models.BooleanField(default=False)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    STATUS_VISIBLE = 'visible'
    STATUS_HIDDEN = 'hidden'
    STATUS_MODERATED = 'moderated'

    STATUS_CHOICES = (
        (STATUS_VISIBLE, 'Visible'),
        (STATUS_HIDDEN, 'Hidden'),
        (STATUS_MODERATED, 'Moderated'),
    )

    post = models.ForeignKey('Post',
                             on_delete=models.CASCADE,
                             related_name='comments')
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    status = models.CharField(max_length=20,
                              default=STATUS_VISIBLE,
                              choices=STATUS_CHOICES)
    moderation_text = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {} (status={})'.format(self.author_name, self.text[:20], self.status)
