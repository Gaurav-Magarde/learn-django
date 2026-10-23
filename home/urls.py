from django.urls import path
from .views import StudentAPIView, ProjectAPIView

# urlpatterns = [
#     path('students/',home),
#     path('projects/', ProjectAPIView.as_view(), name='projects'),
# ]

urlpatterns = [
    path('students/', StudentAPIView.as_view(), name='students'),
    path('projects/', ProjectAPIView.as_view(), name='projects'),

]