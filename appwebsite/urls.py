
from django.urls import path
from . import views 

'''
# Tambien se puede identificar donde importar views
# from appwebsite import views
'''




urlpatterns = [
    path('' , views.home, name='home'),
    # si quiero crear una pagina separada de log in solo quitar el comentario
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
