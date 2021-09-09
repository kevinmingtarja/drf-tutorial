from rest_framework import serializers
from student.models import Student

# Serializer
# class StudentSerializer(serializers.Serializer):
#     nusnet_id = serializers.CharField(max_length=16)
#     name = serializers.CharField(max_length=128)
#     year = serializers.IntegerField()

# ModelSerializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'