
from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [

   path('', views.post_list, name='post_list'),
    # ex: /polls/5/


]


