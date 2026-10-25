from django.urls import path
# from .views import StudentAPIView, ProjectAPIView
from .views import StudentGenericAPIView, StudentUpdateDestroyAPIView,UserRegisterAPIView 

# urlpatterns = [
#     path('students/',home),
#     path('projects/', ProjectAPIView.as_view(), name='projects'),
# ]

urlpatterns = [
    # path('students/', StudentAPIView.as_view(), name='students'),
    # path('projects/', ProjectAPIView.as_view(), name='projects'),
    path('students/', StudentGenericAPIView.as_view(), name='students-list'),
    path('students/<str:id>/', StudentUpdateDestroyAPIView.as_view(), name='students-details'),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
]