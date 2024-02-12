from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.urls import reverse

class Project(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = TaggableManager()
    slug = models.SlugField(max_length=255, unique=True, null=False)

    def __str__(self):

        return self.name

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})

    """
    
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    """