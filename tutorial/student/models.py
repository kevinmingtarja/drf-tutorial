from django.db import models

from faculty.models import Faculty

class Student(models.Model):
    nusnet_id = models.CharField(primary_key=True, max_length=16, blank=False, unique=True)
    name = models.CharField(max_length=128, blank=False)
    year = models.PositiveIntegerField(blank=False)

    faculties = models.ManyToManyField(Faculty, related_name="students_faculties", through="InFaculty")

class InFaculty(models.Model):
    faculty = models.ForeignKey(Faculty, related_name='faculty_to_student', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='student_to_faculty', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('faculty', 'student')
