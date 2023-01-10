from django import forms 
from .models import StoreData,Sale,SaleAmount,Access,ConversionRate


class StoreDataSearchForm(forms.ModelForm):
    class Meta:
        model   = StoreData
        fields  = [ "store" ]


#モデルを使用しないフォームクラス
#https://noauto-nolife.com/post/django-year-month-search-and-list/
class YearForm(forms.Form):
    year    = forms.IntegerField()


class StoreDataForm(forms.ModelForm):
    class Meta:
        model   = StoreData
        fields  = [ "store","date" ]

class SaleForm(forms.ModelForm):
    class Meta:
        model   = Sale
        fields  = ["pc","phone","app","store_data"]

class SaleAmountForm(forms.ModelForm):
    class Meta:
        model   = SaleAmount
        fields  = ["pc","phone","app","store_data"]

class AccessForm(forms.ModelForm):
    class Meta:
        model   = Access
        fields  = ["pc","phone","app","store_data"]

class ConversionRateForm(forms.ModelForm):
    class Meta:
        model   = ConversionRate
        fields  = ["pc","phone","app","store_data"]



