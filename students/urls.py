from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('course/<str:course_code>/enroll', views.enroll, name='enroll'),
    path('course/<str:course_code>/cancel_enroll', views.cancel_enroll, name='cancel_enroll'),
    path('course_list', views.course_list_view, name='course_list'),
    path('course/<str:course_code>', views.course_info, name="course_info"),
]