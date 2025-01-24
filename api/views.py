from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import CarouselBanner, Movie, Category, Series, Banner, Tag
from .serializers import (
    CarouselBannerSerializer, MovieSerializer, CategorySerializer, SeriesSerializer, BannerSerializer
)

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class MoviesByCategoryView(APIView):
    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)
        movies = Movie.objects.filter(category=category)
        serializer = MovieSerializer(movies, many=True)
        return Response({
            'category': category.name,
            'movies': serializer.data
        })

class SeriesByCategoryView(APIView):
    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)
        series = Series.objects.filter(category=category)
        serializer = SeriesSerializer(series, many=True)
        return Response({
            'category': category.name,
            'series': serializer.data
        })

class MovieListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_staff:
            return Response({'error': 'Only admins can upload movies'}, status=status.HTTP_403_FORBIDDEN)

        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SeriesListView(APIView):
    def get(self, request):
        series = Series.objects.all()
        serializer = SeriesSerializer(series, many=True)
        return Response(serializer.data)

class MovieDetailView(APIView):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

class BannerListView(APIView):
    def get(self, request):
        banners = Banner.objects.filter(is_active=True)
        serializer = BannerSerializer(banners, many=True)
        return Response(serializer.data)

class SeriesByCategoryAndTagView(APIView):
    def get(self, request, category_name, tag_name):
        category = get_object_or_404(Category, name__iexact=category_name)
        tag = get_object_or_404(Tag, name__iexact=tag_name)
        series = Series.objects.filter(category=category, tags=tag)  # Use 'tags' here
        serializer = SeriesSerializer(series, many=True)
        return Response(serializer.data)
    
class MoviesByCategoryAndTagView(APIView):
    def get(self, request, category_name, tag_name):
        category = get_object_or_404(Category, name__iexact=category_name)
        tag = get_object_or_404(Tag, name__iexact=tag_name)
        movies = Movie.objects.filter(category=category, tags=tag)  # Use 'tags' here
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
class MoviesByTagAPIView(APIView):
    def get(self, request, tag_name):
        tag = get_object_or_404(Tag, name__iexact=tag_name)  # Fetch the tag
        movies = Movie.objects.filter(tags=tag)  # Use 'tags' here
        series = Series.objects.filter(tags=tag)  # Use 'tags' here

        movies_serializer = MovieSerializer(movies, many=True)
        series_serializer = SeriesSerializer(series, many=True)

        return Response({
            "tag": tag_name,
            "movies": movies_serializer.data,
            "series": series_serializer.data
        })
    

class TagsAPIView(APIView):
    def get(self, request):
        # Fetch all tags from the database
        tags = Tag.objects.all()

        # Create a list of dictionaries for each tag with its associated movies and series
        tags_with_movies_series = []
        for tag in tags:
            # Serialize movies and series using their full serializers
            movies = MovieSerializer(tag.movies.all(), many=True).data
            series = SeriesSerializer(tag.series.all(), many=True).data
            
            # Append the tag name, movies, and series to the list
            tags_with_movies_series.append({
                "tag": tag.name,
                "movies": movies,
                "series": series,
            })

        # Return the tags with their associated movies and series in the response
        return Response(tags_with_movies_series, status=status.HTTP_200_OK)


# class CarouselBannerListView(APIView):
#     def get(self, request):
#         banners = CarouselBanner.objects.filter(is_active=True)
#         serializer = CarouselBannerSerializer(banners, many=True)
#         return Response(serializer.data)

class CarouselBannerListView(APIView):
    def get(self, request):
        # Fetch active carousel banners
        banners = CarouselBanner.objects.filter(is_active=True)
        
        # Serialize the banners
        serializer = CarouselBannerSerializer(banners, many=True)
        
        # Return the serialized data
        return Response(serializer.data)