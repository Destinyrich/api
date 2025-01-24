from rest_framework import serializers
from .models import CarouselBanner, Movie, Category, Series, Season, Episode, Banner
from .models import Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    content_object = serializers.SerializerMethodField()

    def get_content_object(self, obj):
        if isinstance(obj.content_object, Movie):
            return {"type": "movie", "id": obj.content_object.id, "title": obj.content_object.title}
        elif isinstance(obj.content_object, Series):
            return {"type": "series", "id": obj.content_object.id, "title": obj.content_object.title}
        return None

    class Meta:
        model = Banner
        fields = '__all__'


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Season
        fields = ['id', 'season_number', 'title', 'episodes']


class SeriesSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Series
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

# class CarouselBannerSerializer(serializers.ModelSerializer):
#     link = serializers.SerializerMethodField()

#     def get_link(self, obj):
#         if obj.content_object:
#             if isinstance(obj.content_object, Movie):
#                 return {"type": "movie", "id": obj.content_object.id, "title": obj.content_object.title}
#             elif isinstance(obj.content_object, Series):
#                 return {"type": "series", "id": obj.content_object.id, "title": obj.content_object.title}
#         elif obj.external_url:
#             return {"type": "external_url", "url": obj.external_url}
#         return None

#     class Meta:
#         model = CarouselBanner
#         fields = ['id', 'title', 'image', 'is_active', 'link']

# class CarouselBannerSerializer(serializers.ModelSerializer):
#     link = serializers.SerializerMethodField()

#     def get_link(self, obj):
#         if obj.content_object:
#             if isinstance(obj.content_object, Movie):
#                 # Serialize the movie details
#                 return MovieSerializer(obj.content_object).data
#             elif isinstance(obj.content_object, Series):
#                 # Serialize the series details
#                 return SeriesSerializer(obj.content_object).data
#         elif obj.external_url:
#             return {"type": "external_url", "url": obj.external_url}
#         return None

#     class Meta:
#         model = CarouselBanner
#         fields = ['id', 'title', 'image', 'is_active', 'link']

class CarouselBannerSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    def get_link(self, obj):
        if obj.content_object:
            if isinstance(obj.content_object, Movie):
                # Serialize the movie details and add the type field
                movie_data = MovieSerializer(obj.content_object).data
                movie_data['type'] = 'movie'  # Add the type field
                return movie_data
            elif isinstance(obj.content_object, Series):
                # Serialize the series details and add the type field
                series_data = SeriesSerializer(obj.content_object).data
                series_data['type'] = 'series'  # Add the type field
                return series_data
        elif obj.external_url:
            # If it's an external URL, return it with the type field
            return {"type": "external_url", "url": obj.external_url}
        return None

    class Meta:
        model = CarouselBanner
        fields = ['id', 'title', 'image', 'is_active', 'link']