from rest_framework import serializers

from student.models import Student
from faculty.models import Faculty

# Serializer
# class StudentSerializer(serializers.Serializer):
#     nusnet_id = serializers.CharField(max_length=16)
#     name = serializers.CharField(max_length=128)
#     year = serializers.IntegerField()

# ModelSerializer
class StudentSerializer(serializers.ModelSerializer):
    faculties = serializers.PrimaryKeyRelatedField(many=True, queryset=Faculty.objects.all(), read_only=False)

    class Meta:
        model = Student
        fields = '__all__'