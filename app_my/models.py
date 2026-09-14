from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tags')

    def __str__(self):
        return self.name


class Quote(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='quotes')
    text = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='quotes', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quotes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50] 