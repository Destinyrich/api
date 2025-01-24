from django.urls import path
from .views import (
    CarouselBannerListView, MovieListCreateView, MovieDetailView, MoviesByCategoryAndTagView, MoviesByCategoryView, MoviesByTagAPIView, SeriesByCategoryAndTagView,
    SeriesByCategoryView, CategoryListView, BannerListView, SeriesListView, TagsAPIView
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<str:category_name>/movies/', MoviesByCategoryView.as_view(), name='movies-by-category'),
    path('categories/<str:category_name>/series/', SeriesByCategoryView.as_view(), name='series-by-category'),
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
     # Movies filtered by category and tag
    path('categories/<str:category_name>/movies/<str:tag_name>/', MoviesByCategoryAndTagView.as_view(), name='movies-by-category-and-tag'),
      # Series filtered by category and tag
    path('categories/<str:category_name>/series/<str:tag_name>/', SeriesByCategoryAndTagView.as_view(), name='series-by-category-and-tag'),
    path('tags/<str:tag_name>/', MoviesByTagAPIView.as_view(), name='movies_by_tag'),
    path('tags/', TagsAPIView.as_view(), name='tags-list'),  # Maps the URL to the TagsAPIView
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('series/', SeriesListView.as_view(), name='series-list'),
    path('banners/', BannerListView.as_view(), name='banner-list'),
    path('carousel-banners/', CarouselBannerListView.as_view(), name='carousel-banner-list'),

]
