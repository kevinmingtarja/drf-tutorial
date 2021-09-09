from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from student.models import Student
from student.serializers import StudentSerializer

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET', 'POST'])
def hello_world_v2(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

@api_view(['GET'])
def student_detail_manual(request, id):
	student = Student.objects.get(nusnet_id = id)

	return Response({
		"nusnet_id": student.nusnet_id,
		"name": student.name,
		"year": student.year
	})

@api_view(['GET'])
def student_detail_serializer(request, id):
	student = Student.objects.get(nusnet_id = id)
	serializer = StudentSerializer(student)
	return Response(serializer.data)

@api_view(['GET'])
def student_list(request):
	queryset = Student.objects.all()
	serializer = StudentSerializer(queryset, many=True)
	return Response(serializer.data)

class StudentList(generics.ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer