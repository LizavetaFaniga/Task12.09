from django.urls import path
from .views import (
    CategoryView, TagView, QuoteView, RandomQuoteView, 
    QuoteDetailView, UserView, UserDetailView
)

urlpatterns = [
    path('quotes/', QuoteView.as_view()),
    path('quotes/random/', RandomQuoteView.as_view()), 
    path('quotes/<int:pk>/', QuoteDetailView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('tags/', TagView.as_view()),
    path('users/', UserView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
]
