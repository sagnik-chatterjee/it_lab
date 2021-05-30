from django.forms import ModelForm, fields
from .models import ProductInfo


class ProductInfoForm(ModelForm):
    class Meta:
        model = ProductInfo
        fields = "__all__"
