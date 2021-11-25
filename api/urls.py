from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('master/', views.master),                              #####
    path('master/<int:id>', views.masterId),
    path('receiver/', views.ReceiverList.as_view()),             # Опреций Crud для всех моделек
    path('receiver/<int:id>', views.ReceiverDetail.as_view()),
    path('spec/', views.SpecializationList.as_view()),
    path('spec/<int:id>', views.SpecializationDetail.as_view()), #####
    path('master/<int:id>/<str:spec>', views.masterSpec),
    path('masterreceiver/<int:id>/<str:receiver>', views.masterReceiver),
    path('filterMaster/', views.FilterMaster.as_view()),
    path('filterReceiver/', views.FilterReceiver.as_view()),
    path('filterSpec/', views.FilterSpec.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
