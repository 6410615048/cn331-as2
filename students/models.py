from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save      
from django.dispatch import receiver                


class Course(models.Model):
    code = models.CharField(max_length=5)
    course_name = models.CharField(max_length=64)
    semester = models.PositiveSmallIntegerField(choices=((1,1), (2,2), (3,3)))
    year = models.PositiveSmallIntegerField()
    seat = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=5, choices=(("OPEN", "Open"), ("CLOSE", "Close")))
    
    def __str__(self):
        return f"{self.code} : {self.course_name}"

    def enrolled(self):
        if self.status :
            self.seat = self.seat - 1
            if self.seat == 0 :
                self.status = "CLOSE"
            self.save()
            return True
        else :
            return False
    
    def cancel_enroll(self):
        self.seat = self.seat + 1
        if self.seat > 0 :
            self.status = "OPEN"
        self.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True, related_name="students")
    
    def __str__(self):
        return f"{self.user}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not(instance.is_superuser):
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if not(instance.is_superuser):
        instance.profile.save()
