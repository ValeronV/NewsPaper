from django.urls import path
from .views import *

urlpatterns = [
    path('news/', NewsList.as_view(), name='news'),
    path('<slug:post_type>/<int:pk>/', NewDetail.as_view(), name='post_detail'),

    path('news/search/', NewsSearch.as_view(), name='search'),
    path('<slug:post_type>/create/', PostCreate.as_view(), name='post_create'),
    path('<slug:post_type>/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('<slug:post_type>/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

]
