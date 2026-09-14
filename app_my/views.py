from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.views import View
from .models import *

# Create your views here.

class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        category_list = []
        for category in category:
            category_list.append(
                {
                    'id': category.id,
                    'name': category.name,
                    'description': category.description

                }
            )
            obj = {
                'data': category_list
            }
            return JsonResponse(obj)


class TagView(View):
    def get(self, request):
        tags = Tag.objects.all()
        tag_list = []
        for tag in tag:
            tag_list.append(
                {
                    'id': tag.id,
                    'name': tag.name,
                    'created_by': tag.created_by

                }
            )
            obj = {
                'data': tag_list
            }
            return JsonResponse(obj)

class QuoteView(View):
    def get(self, request):
        quoties = Quote.objects.all()
        quote_list = []
        for quote in quote:
            quote_list.append(
                {
                    'id': quote.id,
                    'category': quote.category,
                    'text': quote.text,
                    'tags': quote.tags,
                    'created_by': quote.created_by,
                    'created_at': quote.created_at,
                }
            )
            obj = {
                'data': quote_list
            }
            return JsonResponse(obj)