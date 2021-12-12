from pms import admin
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
import datetime # To Parse input DateTime into Python Date Time Object
import os
from django.conf import settings
from django import forms
from .models import Projects

from pms.models import CustomUser, Staffs, Domains, Projects, Students,StudentFeedback

def student_home(request):
    student_obj = Students.objects.get(admin=request.user.id)
    total_projects=Projects.objects.filter(student_id=student_obj).count()
    context={
        "total_projects":total_projects

    }
    return render(request, "student_template/student_home_template.html",context)



def add_project(request):
    student_obj=Students.objects.get(admin=request.user.id)
    domains = Domains.objects.all()
    staffs = CustomUser.objects.filter(user_type='2')
    project=Projects.objects.filter(student_id=student_obj)
    context = {
        "domains": domains,
        "staffs": staffs,
        "project":project
    }
    return render(request, 'student_template/add_project_template.html', context)



def showdomain(request):
    domains = Domains.objects.all()
    return render(request, "student_template/showdomain.html",{'domains':domains})






def add_project_save(request):
    if request.method != "POST":
        messages.error(request, "Method Not Allowed!")
        return redirect('add_project')
    else:
        project_name = request.POST.get('project')
        domain_id = request.POST.get('domain')
        domain = Domains.objects.get(id=domain_id)
        staff_id = request.POST.get('staff')
        staff = CustomUser.objects.get(id=staff_id)
        
        
        
        project_report = request.FILES['project_report']
        student_obj = Students.objects.get(admin=request.user.id)
        try:
            project = Projects(student_id=student_obj,project_name=project_name, domain_id=domain, staff_id=staff, project_report=project_report)
            project.save()
            messages.success(request, "Project Added Successfully!")
            return redirect('add_project')
        except:
            messages.error(request, "Failed to Add Project!")
            return redirect('add_project')



def manage_project(request):
    student = Students.objects.get(admin=request.user.id)
    projects = Projects.objects.filter(student_id=student.id)
    context = {
        "projects": projects
    }
    return render(request, 'student_template/manage_project_template.html', context)


 
def domaindetails(request,domain_id):
    
    domains = Domains.objects.get(id=domain_id)
    projects = Projects.objects.filter(domain_id=domains)
    context = {
        
       "projects":projects
    }

    return render(request, "student_template/domaindetails.html",context)




def student_search(request , ):
    if request.method == "POST":
        searched = request.POST['searched']
        domains = Domains.objects.filter(domain_name__contains = searched)
        projects = Projects.objects.filter(project_name__contains = searched)
        context = {
            "searched": searched,
            "projects": projects,
            
            "domains": domains
        }
        return render(request, 'student_template/student_search.html', context)
        

    else:
        return render(request, "student_template/student_home_template.html")




# def student_search(request):
#     if request.method == "POST":
#         searched = request.POST['searched']
#         domains =  Domains.objects.filter(name__contains = searched)
#         return render(request, 'student_template/student_search.html', 
#         {'searched': searched ,
#         'domain':domain})
#     else:
#         return render(request, 'student_template/student_search.html', {})




def edit_project(request, project_id):
    project = Projects.objects.get(id=project_id)
    domains = Domains.objects.all()
    staffs = CustomUser.objects.filter(user_type='2')


    context = {
        "project": project,
        "domains": domains,
        "staffs": staffs,
        "id": project_id
    }
    return render(request, 'student_template/edit_project_template.html', context)


def delete_project(request,project_id):
     project = Projects.objects.get(id=project_id)
     try:
        project.delete()
        messages.success(request, "project Deleted Successfully.")
        return redirect('manage_project')
     except:
        messages.error(request, "Failed to Delete project.")
        return redirect('manage_project')






def edit_project_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method.")
    else:
        project_id = request.POST.get('project_id')
        project_name = request.POST.get('project')
        domain_id = request.POST.get('domain')
        staff_id = request.POST.get('staff') 
        project_report = request.FILES['project_report']
                
    

        try:
            project = Projects.objects.get(id=project_id)
            project.project_name = project_name

            domain = Domains.objects.get(id=domain_id)
            project.domain_id = domain

            staff = CustomUser.objects.get(id=staff_id)
            project.staff_id = staff

            if project_report != None:
                project.project_report = project_report
            project.save()


       
          

            messages.success(request, "Project Updated Successfully.")
            # return redirect('/edit_subject/'+subject_id)
            return HttpResponseRedirect(reverse("edit_project", kwargs={"project_id":project_id}))

        except:
            messages.error(request, "Failed to Update Project.")
            return HttpResponseRedirect(reverse("edit_project", kwargs={"project_id":project_id}))
            # return redirect('/edit_subject/'+subject_id)



         














def student_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    student = Students.objects.get(admin=user)

    context={
        "user": user,
        "student": student
    }
    return render(request, 'student_template/student_profile.html', context)


def student_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('student_profile')
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

            student = Students.objects.get(admin=customuser.id)
            student.address = address
            student.save()
            
            messages.success(request, "Profile Updated Successfully")
            return redirect('student_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('student_profile')



def pdf_view(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'r') as fh:
            response = HttpResponse(fh.read(), mimmetype="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
  
        


# def showdomain(request):
#     details=Domains.objects.all()
#     return render(request, "student_template/showdomain.html",{'domains':details})

# def domaindetails(request,domain_id):
#     domains = Domains.object.get(id=domain_id)
#     return render(request, "student_template/domaindetails.html",{'domains':domains})



def studentfeedback(request):
    student_obj=Students.objects.get(admin=request.user.id)
    feedback_data=StudentFeedback.objects.filter(student_id=student_obj)
    return render(request,'student_template/studentsfeedback.html',{"feedback_data":feedback_data})


def student_feedback_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method.")
        return redirect('student_feedback')
    else:
        feedback=request.POST.get('feedback_message')
        student_obj=Students.objects.get(admin=request.user.id)
        try:
            add_feedback=StudentFeedback(student_id=student_obj,message=feedback,message_reply="")
            add_feedback.save()
            messages.success(request, "Feedback Sent.")
            return redirect('studentfeedback')
        except:
            messages.error(request, "Failed to Send Feedback.")
            return redirect('studentfeedback')


def student_view_result(request):
    student = Students.objects.get(admin=request.user.id)
    projects = Projects.objects.filter(student_id=student.id)
    context = {
        "projects": projects
    }
    return render(request, "student_template/student_view_result.html", context)

