from django.urls import path, include
from ns_app.views import index, about

urlpatterns = [
    path('', about),
    # path('about/<int:num1>+<int:num2>', about),
]
