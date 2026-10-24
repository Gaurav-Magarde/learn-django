from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from .models import Student,Project
from .serializers import StudentSerializer, ProjectSerializer
# # Create your views here.
# @api_view(['GET','POST','DELETE'])
# def home(request):
#     student_id = request.data.get('id')

#     if request.method == 'GET':
#         query = request.query_params.get('search')
#         if query:
#             student = Student.objects.filter(name__icontains=query)
#         else:
#             student = Student.objects.all()
#         serializer = StudentSerializer(student,many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=201)
#         return Response(serializer.errors,status=400)
    
#     if request.method == 'DELETE':
#         if not student_id:
#             return Response({'error':'Student ID is required'},status=400)
#         try:
#             student = Student.objects.get(id=student_id)
#         except Student.DoesNotExist:
#             return Response({'error':'Student not found'},status=404)
#         student.delete()
#         return Response(status=204)

# class StudentAPIView(APIView):
#     def get(self,request):
#         student = Student.objects.all()
#         serializer = StudentSerializer(student,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=201)
#         return Response(serializer.errors,status=400)

#     def delete(self,request):
#         student_id = request.data.get('id')
#         if not student_id:
#             return Response({'error':'Student ID is required'},status=400)
#         try:
#             student = Student.objects.get(id=student_id)
#         except Student.DoesNotExist:
#             return Response({'error':'Student not found'},status=404)
#         student.delete()
#         return Response(status=204)
#     def put(self,request):
#         student_id = request.data.get('id')
#         if not student_id:
#             return Response({'error':'Student ID is required'},status=400)
#         try:
#             student = Student.objects.get(id=student_id)
#         except Student.DoesNotExist:
#             return Response({'error':'Student not found'},status=404)
#         serializer = StudentSerializer(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=200)
#         return Response(serializer.errors,status=400)
#     def patch(self,request):
#         student_id = request.data.get('id')
#         if not student_id:
#             return Response({'error':'Student ID is required'},status=400)
#         try:
#             student = Student.objects.get(id=student_id)
#         except Student.DoesNotExist:
#             return Response({'error':'Student not found'},status=404)
#         serializer = StudentSerializer(student,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=200)
#         return Response(serializer.errors,status=400)   

# class ProjectAPIView(APIView):
#     def get(self,request):
#         project = Project.objects.all()
#         serializer = ProjectSerializer(project,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = ProjectSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=201)
#         return Response(serializer.errors,status=400)
#     def delete(self,request):
#         project_id = request.data.get('id')
#         if not project_id:
#             return Response({'error':'Project ID is required'},status=400)
#         try:
#             project = Project.objects.get(id=project_id)
#         except Project.DoesNotExist:
#             return Response({'error':'Project not found'},status=404)
#         project.delete()
#         return Response(status=204)
#     def put(self,request):
#         project_id = request.data.get('id')
#         if not project_id:
#             return Response({'error':'Project ID is required'},status=400)
#         try:
#             project = Project.objects.get(id=project_id)
#         except Project.DoesNotExist:
#             return Response({'error':'Project not found'},status=404)
#         serializer = ProjectSerializer(project,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=200)
#         return Response(serializer.errors,status=400)
#     def patch(self,request):
#         project_id = request.data.get('id')
#         if not project_id:
#             return Response({'error':'Project ID is required'},status=400)
#         try:
#             project = Project.objects.get(id=project_id)
#         except Project.DoesNotExist:
#             return Response({'error':'Project not found'},status=404)
#         serializer = ProjectSerializer(project,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=200)
#         return Response(serializer.errors,status=400)   

class StudentGenericAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'
    