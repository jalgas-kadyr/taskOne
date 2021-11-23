from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('masters/', views.masterList),
    path('addMaster/', views.addMaster),
    path('master/<int:id>/', views.masterDetail),
    path('changeMaster/<int:id>/', views.changeMaster)
    # path('snippets/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
