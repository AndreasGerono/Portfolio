from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    date = models.DateField()
    slug = models.SlugField(max_length=300, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']
