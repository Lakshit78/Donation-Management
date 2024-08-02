from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('login/',views.user_login,name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('truehome/',views.truehome,name='truehome'),
    path('history/',views.history,name='history'),
    path('cloths/',views.cloths,name='cloths'),
    path('apple/',views.apple,name='apple'),
    path('banana/',views.banana,name='banana'),
    path('children/',views.children,name='children'),
    path('studentregister/',views.studentregister,name='studentregister'),
    path('banana/', views.banana, name='banana'),
    path('send_email/', views.send_email, name='send_email'),
]

