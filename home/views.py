from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
# Create your views here.
@api_view(['GET','POST','DELETE'])
def home(request):
    student_id = request.data.get('id')

    if request.method == 'GET':
        query = request.query_params.get('search')
        if query:
            student = Student.objects.filter(name__icontains=query)
        else:
            student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
    if request.method == 'DELETE':
        if not student_id:
            return Response({'error':'Student ID is required'},status=400)
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error':'Student not found'},status=404)
        student.delete()
        return Response(status=204)