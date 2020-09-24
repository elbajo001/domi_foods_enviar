from django.urls import path
from .views import *


urlpatterns = [
    #path('', ProductAPIView.as_view()),
    path('<int:pk>/', GETDetailRestaurant.as_view()),
    #path('<int:pk>/', GETDetailCategoryRestaurant.as_view()),
    path('', GETListRestaurant.as_view()),
    path('v1/<int:pk>/', POSTDetailRestaurant.as_view()),
    path('v1', POSTListRestaurant.as_view()),
]
