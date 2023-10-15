from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .models import Course, Profile

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if not request.user.is_superuser :
        profile = Profile.objects.get(user=request.user)
        return render(request, 'students/index.html', {
            'profile' : profile,
            'courses' : profile.courses.all(),
            'non_courses' : Course.objects.exclude(id__in=profile.courses.all())
                            .exclude(status="CLOSE").all()
        })
    else :
        return render(request, 'students/index2.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'students/login.html', {
                'message': 'Invalid credentials.'
            })

    return render(request, "students/login.html")


def logout_view(request):
    logout(request)
    return render(request, 'students/login.html', {
        'message': 'Logged out'
    })
    
def course_list_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    profile = Profile.objects.get(user=request.user)
    return render(request, "students/course_list.html", {
        'courses': profile.courses.all(),
        'non_courses' : Course.objects.exclude(id__in=profile.courses.all())
                            .exclude(status="CLOSE").all(),
    })

def course_info(request, course_code):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    course = Course.objects.get(code=course_code)
    profile = Profile.objects.get(user=request.user)
    check = profile.courses.filter(pk = course.id).count() != 0
    return render(request, "students/course_info.html", {
        'course': course,
        'check' : check,
    })

def enroll(request, course_code):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        course = Course.objects.get(code = course_code) 
        check = course.enrolled()
        if check :
            profile.courses.add(course)
        return render(request, "students/course_list.html", {
            'courses': profile.courses.all(),
            'non_courses' : Course.objects.exclude(id__in=profile.courses.all())
                            .exclude(status="CLOSE").all(),
        })

def cancel_enroll(request, course_code):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        course = Course.objects.get(code = course_code)
        course.cancel_enroll()
        profile.courses.remove(course)
        return render(request, "students/course_list.html", {
            'courses': profile.courses.all(),
            'non_courses' : Course.objects.exclude(id__in=profile.courses.all())
                                .exclude(status="CLOSE").all(),
        })