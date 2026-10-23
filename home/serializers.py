from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll_number','city']
        read_only_fields = ['id'] 

    def validate_name(self,value):
        if len(value) < 3:
            raise serializers.ValidationError('Name should be at least 3 characters long')
        return value

    def validate_roll_number(self,value):
        if value >100:
            raise serializers.ValidationError('Roll number should be less than 100')
        return value