from django.db.models.base import Model
from django.forms import ModelForm, fields
from .models import Category, Page


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = "__all__"
