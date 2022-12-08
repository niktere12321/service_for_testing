from django.contrib.auth.decorators import login_required
from django.urls import path
from django.urls import re_path as url

from . import views

app_name = 'testing'


urlpatterns = [
    path('get-result/<int:pk>/', login_required(views.GetResult.as_view()), name='get_result'),
    url(r'^testing/', views.testing, name='testing'),
    url(r'^', login_required(views.Index.as_view()), name='index'),
]
