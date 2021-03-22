import os
import PIL
from django.db import models
from django.template.defaultfilters import slugify


class Article(models.Model):
    is_draft = models.BooleanField(default=False)
    title = models.CharField(max_length=300)
    text = models.TextField(blank=True)
    date = models.DateField()
    slug = models.SlugField(max_length=300, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


def get_image_path(instance, filename):
    return os.path.join('media', instance.article.slug, filename)


class Image(models.Model):
    image = models.ImageField(upload_to=get_image_path)
    alt = models.CharField(max_length=100, default='')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Remove Exif data!
        image = PIL.Image.open(self.image.path)
        image.save(self.image.path)
