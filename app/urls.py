
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home,name="home"), # main index page
    path('favorite/', views.favorite,name="favorite"),
    path('profile/<str:pk>', views.profile,name="profile"),
    path('edit/', views.edit_contacts,name="edit"),
    path('delete/<str:pk>', views.delete_contact,name="delete"),
    path('search/', views.SearchResultView, name="search"),
]
