from pms import admin
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


from pms.models import CustomUser, Staffs, Domains, Projects, Students,StudentsResult


def staff_home(request):
     return render(request, "staff_template/staff_home_template.html")

   



def staff_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    staff = Staffs.objects.get(admin=user)

    context={
        "user": user,
        "staff": staff
    }
    return render(request, 'staff_template/staff_profile.html', context)
    


def staff_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('staff_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()

            staff = Staffs.objects.get(admin=customuser.id)
            staff.address = address
            staff.save()

            messages.success(request, "Profile Updated Successfully")
            return redirect('staff_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('staff_profile')


def staff_add_result(request):
    
    staffs = request.user
    projects = Projects.objects.filter(staff_id=staffs.id)
    context = {
        "projects": projects
    }
    return render(request, 'staff_template/staff_add_result.html', context)


# def check_project(request,project_id):
#     pass

def check_project(request, project_id):
    project = Projects.objects.get(id=project_id)
    domains = Domains.objects.all()
    


    context = {
        "project": project,
        "domains": domains,
        
        "id": project_id
    }
    return render(request, 'staff_template/check_project.html', context)

def check_project_save(request,project_id):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('staff_add_result')
    else:
        
        miniproject_marks = request.POST.get('miniproject_marks')
        
        
        

        try:
            # Check if Students Result Already Exists or not
            check_exist = Projects.objects.filter(id=project_id).exists()
            if check_exist:
                result = Projects.objects.get(id=project_id)
                result.miniproject_marks = miniproject_marks
                
                result.save()
                messages.success(request, "Result Updated Successfully!")
                return redirect('staff_add_result')
            else:
                result = Projects.objects.get(id=project_id)
                result.miniproject_marks = miniproject_marks
                
                
                result.save()
                messages.success(request, "Result Added Successfully!")
                return redirect('staff_add_result')
        except:
            messages.error(request, "Failed to Add Result!")
            return redirect('staff_add_result')
