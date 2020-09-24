from django.urls import path
from .views import *


urlpatterns = [
    #path('', ProductAPIView.as_view()),
    path('<int:pk>/', GETDetailProduct.as_view()),
    path('', GETListProduct.as_view()),
    path('v1/<int:pk>/', POSTDetailProduct.as_view()),
    path('v1', POSTListProduct.as_view()),
]
