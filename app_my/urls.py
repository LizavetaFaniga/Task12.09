from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('categories/', views.CategoryView.as_view(), name='category_list'),
    path('tags/', views.TagView.as_view(), name='tag_list'),
    path('quotes/', views.QuoteView.as_view(), name='quote_list'),
]
