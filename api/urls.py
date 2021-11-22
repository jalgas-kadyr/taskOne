from django.urls import path
from api import views

urlpatterns = [
    path('masters/', views.masterList),
    path('master/<str:name>/', views.master)
    # path('snippets/<int:pk>/', views.snippet_detail),
]