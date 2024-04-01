from django.db import models
from django.forms import DateTimeInput
from django_filters import *
from .models import *


class PostFilter(FilterSet):
    title=CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Заголовок'
    )

    post_type = ChoiceFilter(label='Тип', choices=ptype)

    added_after = DateTimeFilter(
        field_name='post_data_time',
        lookup_expr='gt',
        label='Дата от',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
