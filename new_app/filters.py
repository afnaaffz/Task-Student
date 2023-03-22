import django_filters
from django.forms import TextInput
from django_filters import CharFilter

from new_app.models import StudentRegister


class NameFilter(django_filters.FilterSet):
    username = CharFilter(field_name='username',label='',lookup_expr="icontains",widget=TextInput(attrs={'placeholder':'Search by Name'}))
    class Meta:
        model = StudentRegister
        fields = ('username',)