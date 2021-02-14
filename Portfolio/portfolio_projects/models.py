from django.db import models
from django.template.defaultfilters import slugify
import PIL
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


class Image(models.Model):
    tag = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/%Y/%m/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Remove Exif data!
        image = PIL.Image.open(self.image.path)
        image.save(self.image.path)
