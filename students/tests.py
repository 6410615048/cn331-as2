from django.test import TestCase
from .models import Course, Profile
from django.contrib.auth.models import User

class Testing(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='4', email='', password='Student331')
        student4 = Profile.objects.get(user=user)
    
        course1 = Course.objects.create(code="CN111",
                                    course_name="1",
                                    semester = 1,
                                    year = "2023",
                                    seat = 1,
                                    status = "OPEN")
    
    def test_student_list_empty(self):
        course = Course.objects.get(code = 'CN111')
        
        self.assertIsNone(course.get_student().first())
    
    def test_student_list(self):
        student = Profile.objects.get(user = User.objects.get(username='4'))
        course = Course.objects.get(code = 'CN111')
        student.courses.add(course)
        
        self.assertEqual(course.get_student().first(), student)