import os
import PIL
from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


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

    def last():
        last = Article.objects.all().order_by('-pk').first()
        if last is not None:
            return last.slug
        return 'default'

    class Meta:
        ordering = ['-date']


def get_image_path(instance, filename):
    return os.path.join('images', 'articles', filename)


class Image(models.Model):
    image = models.ImageField(upload_to='media')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Remove Exif data!
        image = PIL.Image.open(self.image.path)
        image.save(self.image.path)
