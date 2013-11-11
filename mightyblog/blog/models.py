from datetime import datetime

from django.db import models
from tagging.fields import TagField
from tagging.utils import parse_tag_input
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length = 127)
    description = models.CharField(max_length = 255)
    date_created = models.DateTimeField(default = datetime.now())
    date_modefied = models.DateTimeField(default = datetime.now())
    content = HTMLField()
    tags = TagField()

    def __unicode__(self):
        return "%s | (%d,%d,%d)" % (self.title, self.date_created.day,
                                    self.date_created.month, self.date_created.year)

    def get_absolute_url(self):
        return "/post/" + str(self.pk) + "/" + self.title.replace(' ', '-')

    def get_tag_list(self):
        return parse_tag_input(self.tags)

    @staticmethod
    def get_top_rated():
        return Post.objects.all()[:10]

class Comment(models.Model):
    author = models.CharField(max_length = 63)
    post = models.ForeignKey(Post)
    email = models.EmailField(null = True, blank = True)
    website = models.URLField(null = True, blank = True)
    text = models.TextField(max_length = 255)

    def __unicode__(self):
        return "%s: %s.." % (self.author, self.text[:10])

class Category(models.Model):
    name = models.CharField(max_length = 63)
    description = models.CharField(max_length = 255)
    posts = models.ManyToManyField(Post, null = True, blank = True)
    tags = TagField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/category/" + self.name.replace(' ', '-')


class Project(models.Model):
    name = models.CharField(max_length = 63)
    related_posts = models.ManyToManyField(Post)
    github_url = models.URLField(null = True, blank = True)
    content = HTMLField()
    tags = TagField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/project/" + str(self.pk) + "/" + self.name.replace(' ', '-')

