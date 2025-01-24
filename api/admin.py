from django.contrib import admin
from .models import Banner, CarouselBanner, Episode, Movie, Season, Series, Category, Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date', 'rating', 'get_tags')  # Corrected
    search_fields = ('title', 'genre')
    list_filter = ('genre', 'release_date')

    def get_tags(self, obj):
        """Display tags as a comma-separated list."""
        return ", ".join(tag.name for tag in obj.tags.all())
    get_tags.short_description = 'Tags'


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'image', 'banner', 'get_tags')  # Corrected
    search_fields = ('title',)
    list_filter = ('release_date',)

    def get_tags(self, obj):
        """Display tags as a comma-separated list."""
        return ", ".join(tag.name for tag in obj.tags.all())
    get_tags.short_description = 'Tags'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'image', 'content_object')
    search_fields = ('title',)
    list_filter = ('is_active',)
    ordering = ('-is_active',)


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('series', 'title', 'season_number')
    search_fields = ('title', 'series__title')
    list_filter = ('series',)


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'season', 'episode_number', 'release_date')
    search_fields = ('title', 'season__title')
    list_filter = ('season',)


@admin.register(CarouselBanner)
class CarouselBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'content_type', 'object_id', 'external_url')
    search_fields = ('title',)
    list_filter = ('is_active',)
    ordering = ('-is_active',)