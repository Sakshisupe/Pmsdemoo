


from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)



class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at=models.DateTimeField(default=now,blank=True)
    updated_at=models.DateTimeField(default=now,blank=True)
    objects = models.Manager()


class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



class Domains(models.Model):
    id = models.AutoField(primary_key=True)
    domain_name = models.CharField(max_length=255)
    created_at=models.DateTimeField(default=now,blank=True)
    updated_at=models.DateTimeField(default=now,blank=True)
    objects = models.Manager()








class Students(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.TextField()
    created_at=models.DateTimeField(default=now,blank=True)
    updated_at=models.DateTimeField(default=now,blank=True)
    objects = models.Manager()


class Projects(models.Model):
    id =models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    domain_id = models.ForeignKey(Domains, on_delete=models.CASCADE, default=1 , related_name="domain_fk") #need to give defauult course
    staff_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    student_id=models.ForeignKey(Students,on_delete=CASCADE,null=True)
    project_report = models.FileField(upload_to='pdf')
    miniproject_marks=models.FloatField(default=0)
    created_at=models.DateTimeField(default=now,blank=True)
    updated_at=models.DateTimeField(default=now,blank=True)
    objects = models.Manager()

class StudentFeedback(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=CASCADE)
    message=models.CharField(max_length=250)
    message_reply=models.CharField(max_length=265)
    created_at=models.DateTimeField(default=now,blank=True)
    updated_at=models.DateTimeField(default=now,blank=True)
    objects = models.Manager()


class StudentsResult(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    staff_id=models.ForeignKey(Staffs,models.CASCADE)
    project_id=models.ForeignKey(Projects,models.CASCADE)
    domain_id=models.ForeignKey(Domains,on_delete=CASCADE)
    miniproject_marks=models.FloatField(default=0)
    created_at=models.DateTimeField(default=now,blank=True)
    updated_at=models.DateTimeField(default=now,blank=True)
    objects = models.Manager()
    





#Creating Django Signals

# It's like trigger in database. It will run only when Data is Added in CustomUser model

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance)
        if instance.user_type == 3:
            Students.objects.create(admin=instance)
    

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.staffs.save()
    if instance.user_type == 3:
        instance.students.save()
    


