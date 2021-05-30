from django.db import models

# Create your models here.


class Category(models.Model):
    """
    a name, number of visits, and number of likes.
    """

    name = models.CharField(max_length=200)
    visit_count = models.IntegerField()
    like_count = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.visit_count + " " + self.like_count


class Page(models.Model):
    """
    to a category, has a title, URL, and many views.
    """

    category = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    url = models.URLField()
    view_count = models.IntegerField()

    def __str__(self):
        return self.title + "" + self.url
