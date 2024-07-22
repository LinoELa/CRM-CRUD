
from django.urls import path
from . import views 

'''
# Tambien se puede identificar donde importar views
# from appwebsite import views
'''




urlpatterns = [
    path('' , views.home, name='home'),
]
