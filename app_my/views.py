from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Category, Tag, Quote
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from json import loads
from .forms import CategoryForm, TagForm, QuoteForm, UserForm

User = get_user_model()


@method_decorator(csrf_exempt, 'dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        category_list = []
        for category in categories:
            category_list.append({
                'id': category.id,
                'name': category.name,
                'description': category.description
            })
        obj = {'data': category_list}
        return JsonResponse(obj)

    def post(self, request):
        raw_json = request.body
        new_data = loads(raw_json)
        
        form = CategoryForm(new_data)
        
        if form.is_valid():
            form.save()
            return self.get(request)
        else:
            return JsonResponse(
                {'status': 'error', 'code': 400},
                status=400
            )


@method_decorator(csrf_exempt, 'dispatch')
class TagView(View):
    def get(self, request):
        tags = Tag.objects.all()
        tag_list = []
        for tag in tags:
            tag_list.append({
                'id': tag.id,
                'name': tag.name,
                'created_by': tag.created_by.username
            })
        obj = {'data': tag_list}
        return JsonResponse(obj)

    def post(self, request):
        raw_json = request.body
        new_data = loads(raw_json)
        
        form = TagForm(new_data)
        
        if form.is_valid():
            form.save()
            return self.get(request)
        else:
            return JsonResponse(
                {'status': 'error', 'code': 400},
                status=400
            )


@method_decorator(csrf_exempt, 'dispatch')
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

    def post(self, request):
        raw_json = request.body
        new_data = loads(raw_json)
        
        form = QuoteForm(new_data)
        
        if form.is_valid():
            form.save()
            return self.get(request)
        else:
            return JsonResponse(
                {'status': 'error', 'code': 400},
                status=400
            )


@method_decorator(csrf_exempt, 'dispatch')
class RandomQuoteView(View):
    def get(self, request):
        quote = Quote.objects.select_related('category', 'created_by').prefetch_related('tags').order_by('?').first()
        if not quote:
            return JsonResponse({'error': 'Цитаты не найдены'}, status=404)
        quote_data = {
            'id': quote.id,
            'text': quote.text,
            'category': quote.category.name if quote.category else None,
            'tags': [tag.name for tag in quote.tags.all()],
            'created_by': quote.created_by.username,
            'created_at': quote.created_at.isoformat(),
        }
        return JsonResponse({'data': quote_data})


@method_decorator(csrf_exempt, 'dispatch')
class QuoteDetailView(View):
    def get(self, request, pk):
        quote = get_object_or_404(
            Quote.objects.select_related('category', 'created_by').prefetch_related('tags'), 
            id=pk
        )
        quote_data = {
            'id': quote.id,
            'text': quote.text,
            'category': quote.category.name if quote.category else None,
            'tags': [tag.name for tag in quote.tags.all()],
            'created_by': quote.created_by.username,
            'created_at': quote.created_at.isoformat(),
        }
        return JsonResponse({'data': quote_data})


@method_decorator(csrf_exempt, 'dispatch')
class UserView(View):
    def get(self, request):
        users = User.objects.all()
        user_list = []
        for user in users:
            user_list.append({
                'id': user.id,
                'username': user.username,
                'email': user.email, 
            })
        obj = {'data': user_list}
        return JsonResponse(obj)

    def post(self, request):
        raw_json = request.body
        new_data = loads(raw_json)
        
        form = UserForm(new_data)
        
        if form.is_valid():
            form.save()
            return self.get(request)
        else:
            return JsonResponse(
                {'status': 'error', 'code': 400},
                status=400
            )


@method_decorator(csrf_exempt, 'dispatch')
class UserDetailView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        }
        return JsonResponse({'data': user_data})