from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Import slugify to generate slugs from strings
from django.utils.text import slugify


class Profile(models.Model):
    name = models.CharField(max_length=200, blank=True)
    profession = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="add about your work and contact",
                           max_length=300)
    slug = models.SlugField(blank=True, unique=True)
    email = models.EmailField(max_length=200, blank=True)
    county = models.CharField(max_length=200, blank=True)
    avatar = CloudinaryField('image', default='placeholder')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}"


class Meta:
    ordering = ['created_on']

    def __str__(self):
        return str(self.username)


class Review(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                related_name="reviews")
    first_name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.first_name}"
