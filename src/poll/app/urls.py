from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('vote/<int:id>/',views.vote,name='vote'),
    path('view/<int:id>/',views.view,name = 'view'),
    path('delete/<int:id>',views.delete,name = 'delete'),
]
