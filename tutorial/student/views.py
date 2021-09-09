from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from student.models import Student
from student.serializers import StudentSerializer


@api_view() # Defaults to GET request since we don't specify anything
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET', 'POST']) # Able to process GET and POST request
def hello_world_v2(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

# Less preferred compared to student_detail_serializer. Because why do it manually if we can do it automatically.
@api_view(['GET'])
def student_detail_manual(request, id):
	student = Student.objects.get(nusnet_id = id)

	return Response({
		"nusnet_id": student.nusnet_id,
		"name": student.name,
		"year": student.year
	})

# More preferred way
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

# Uses Generics to simplify our code, while having the same functionalities. 
class StudentList(generics.ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer