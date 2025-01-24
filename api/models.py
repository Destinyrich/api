from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100,)
    description = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()
    genre = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    video_file = models.FileField(upload_to='videos/original/', blank=True, null=True)
    video_360p = models.FileField(upload_to='videos/360p/', blank=True, null=True)
    video_480p = models.FileField(upload_to='videos/480p/', blank=True, null=True)
    video_720p = models.FileField(upload_to='videos/720p/', blank=True, null=True)
    video_1080p = models.FileField(upload_to='videos/1080p/', blank=True, null=True)
    streaming_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movies')
    views = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name='movies',blank=True)  # Add this line

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='banners/')
    is_active = models.BooleanField(default=True)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.SET_NULL, blank=True, null=True
    )
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.title


class Series(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    banner = models.ForeignKey(Banner, on_delete=models.SET_NULL, blank=True, null=True)
    release_date = models.DateField()
    genre = models.CharField(max_length=100, default='Unknown')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='series_images/', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='series',blank=True)  # Add this line

    def __str__(self):
        return self.title


class Season(models.Model):
    series = models.ForeignKey(Series, related_name='seasons', on_delete=models.CASCADE)
    season_number = models.PositiveIntegerField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"Season {self.season_number} of {self.series.title}"


class Episode(models.Model):
    season = models.ForeignKey(Season, related_name='episodes', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    episode_number = models.PositiveIntegerField()
    video_file = models.FileField(upload_to='episodes/original/')
    video_360p = models.FileField(upload_to='episodes/360p/', blank=True, null=True)
    video_480p = models.FileField(upload_to='episodes/480p/', blank=True, null=True)
    video_720p = models.FileField(upload_to='episodes/720p/', blank=True, null=True)
    video_1080p = models.FileField(upload_to='episodes/1080p/', blank=True, null=True)
    release_date = models.DateField()

    def __str__(self):
        return f"Episode {self.episode_number}: {self.title}"


class CarouselBanner(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='carousel_banners/')
    is_active = models.BooleanField(default=True)
    
    # Link options
    content_type = models.ForeignKey(
        ContentType, on_delete=models.SET_NULL, blank=True, null=True
    )  # For Movie or Series
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    external_url = models.URLField(blank=True, null=True)  # For external links

    def __str__(self):
        return self.title
