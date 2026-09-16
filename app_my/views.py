from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.views import View
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt, 'dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        category_list = []
        for category in categories:
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

    def post(self, request): 
        


class TagView(View):
    def get(self, request):
        tags = Tag.objects.all()
        tag_list = []
        for tag in tags:
            tag_list.append(
                {
                    'id': tag.id,
                    'name': tag.name,
                    'created_by': tag.created_by.username

                }
            )
        obj = {
            'data': tag_list
        }
        return JsonResponse(obj)

class QuoteView(View):
    def get(self, request):
        quotes = Quote.objects.select_related('category', 'created_by').prefetch_related('tags')
        quote_list = []
        for quote in quotes:
            quote_list.append({
                'id': quote.id,
                'text': quote.text,
                'category': quote.category.name if quote.category else None,
                'tags': [tag.name for tag in quote.tags.all()],
                'created_by': quote.created_by.username,
                'created_at': quote.created_at.isoformat(),
            })
        return JsonResponse({'data': quote_list})