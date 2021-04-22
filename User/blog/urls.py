from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register , name='user-register'),
    path('login/', views.login , name='user-login'),
    path('profile/', views.profile , name='user-profile'),
    path('update/', views.update , name='user-update'),
    path('identify/', views.identify , name='user-identify')

]
