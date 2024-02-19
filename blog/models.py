from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify

class Project(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()

    repo = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='images/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = TaggableManager()
    slug = models.SlugField(max_length=255, unique=True, null=False)

    APPLICATION = "Application"
    GAME = "Game"

    TYPE_CHOICES = (

        (APPLICATION, "Application"),
        (GAME, "Game")

    )

    project_type = models.TextField(choices=TYPE_CHOICES, default=APPLICATION)

    def __str__(self):

        return self.name

    def save(self, *args, **kwargs):
        
        if not self.id: # this prevents broken links with url update so this function will work only when object creating

            self.slug = slugify(self.name)

        self.description_short = self.description[:180] + ' ...' if len(self.description) > 100 else self.description 
        super(Project, self).save(*args, **kwargs)


    """
    
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):

        self.published_date = timezone.now()
        self.save()
    
    """