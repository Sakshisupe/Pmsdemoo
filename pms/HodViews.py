from pms.StudentViews import domaindetails
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from pms.models import CustomUser, Staffs, Domains, Projects,Students,StudentFeedback


def admin_home(request):
    student_obj = Students.objects.all().count()
    staff_obj=Staffs.objects.all().count()
    domaindetails_obj=Domains.objects.all().count()
    context={
        "student_obj":student_obj,
        "domaindetails_obj":domaindetails_obj,
        "staff_obj":staff_obj

        

    }
    return render(request, "hod_template/home_content.html",context)


def add_staff(request):
    return render(request, "hod_template/add_staff_template.html")


def add_staff_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_staff')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            user.staffs.address = address
            user.save()
            messages.success(request, "Staff Added Successfully!")
            return redirect('add_staff')
        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('add_staff')



def manage_staff(request):
    staffs = Staffs.objects.all()
    context = {
        "staffs": staffs
    }
    return render(request, "hod_template/manage_staff_template.html", context)


def edit_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)

    context = {
        "staff": staff,
        "id": staff_id
    }
    return render(request, "hod_template/edit_staff_template.html", context)


def edit_staff_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get('staff_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            # INSERTING into Staff Model
            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()

            messages.success(request, "Staff Updated Successfully.")
            return redirect('/edit_staff/'+staff_id)

        except:
            messages.error(request, "Failed to Update Staff.")
            return redirect('/edit_staff/'+staff_id)



def delete_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    try:
        staff.delete()
        messages.success(request, "Staff Deleted Successfully.")
        return redirect('manage_staff')
    except:
        messages.error(request, "Failed to Delete Staff.")
        return redirect('manage_staff')




def add_domain(request):
    return render(request, "hod_template/add_domain_template.html")


def add_domain_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_domain')
    else:
        domain = request.POST.get('domain')
        try:
            domain_model = Domains(domain_name=domain)
            domain_model.save()
            messages.success(request, "Domain Added Successfully!")
            return redirect('add_domain')
        except:
            messages.error(request, "Failed to Add Domain!")
            return redirect('add_domain')


def manage_domain(request):
    domains = Domains.objects.all()
    context = {
        "domains": domains
    }
    return render(request, 'hod_template/manage_domain_template.html', context)


def edit_domain(request, domain_id):
    domain = Domains.objects.get(id=domain_id)
    context = {
        "domain": domain,
        "id": domain_id
    }
    return render(request, 'hod_template/edit_domain_template.html', context)


def edit_domain_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        domain_id = request.POST.get('domain_id')
        domain_name = request.POST.get('domain')

        try:
            domain = Domains.objects.get(id=domain_id)
            domain.domain_name = domain_name
            domain.save()

            messages.success(request, "Domain Updated Successfully.")
            return redirect('/edit_domain/'+domain_id)

        except:
            messages.error(request, "Failed to Update Course.")
            return redirect('/edit_domain/'+domain_id)


def delete_domain(request, domain_id):
    domain = Domains.objects.get(id=domain_id)
    try:
        domain.delete()
        messages.success(request, "domain Deleted Successfully.")
        return redirect('manage_domain')
    except:
        messages.error(request, "Failed to Delete domain.")
        return redirect('manage_domain')





































def add_student(request):
    return render(request, "hod_template/add_student_template.html")


def add_student_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_student')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
            user.students.address = address
            user.save()
            messages.success(request, "Student Added Successfully!")
            return redirect('add_student')
        except:
            messages.error(request, "Failed to Add Student!")
            return redirect('add_student')



def manage_student(request):
    students = Students.objects.all()
    context = {
        "students": students
    }
    return render(request, "hod_template/manage_student_template.html", context)


def edit_student(request, student_id):
    student = Students.objects.get(admin=student_id)

    context = {
        "student": student,
        "id": student_id
    }
    return render(request, "hod_template/edit_student_template.html", context)


def edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        student_id = request.POST.get('student_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            # INSERTING into Staff Model
            student_model = Students.objects.get(admin=student_id)
            student_model.address = address
            student_model.save()

            messages.success(request, "Student Updated Successfully.")
            return redirect('/edit_student/'+student_id)

        except:
            messages.error(request, "Failed to Update Student.")
            return redirect('/edit_student/'+student_id)



def delete_student(request, student_id):
    student = Students.objects.get(admin=student_id)
    try:
        student.delete()
        messages.success(request, "Student Deleted Successfully.")
        return redirect('manage_student')
    except:
        messages.error(request, "Failed to Delete Student.")
        return redirect('manage_student')
















































@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)



@csrf_exempt

def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context={
        "user": user
    }
    return render(request, 'hod_template/admin_profile.html', context)


def admin_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('admin_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('admin_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('admin_profile')
    


def staff_profile(request):
    pass


def student_profile(requtest):
    pass




def student_feedback_message(request):
    feedbacks = StudentFeedback.objects.all()
    context = {
        "feedbacks": feedbacks
    }
    return render(request, 'hod_template/student_feedback_template.html', context)


@csrf_exempt
def student_feedback_message_reply(request):
    feedback_id = request.POST.get('id')
    feedback_reply = request.POST.get('reply')

    try:
        feedback = StudentFeedback.objects.get(id=feedback_id)
        feedback.message_reply = feedback_reply
        feedback.save()
        return HttpResponse("True")

    except:
        return HttpResponse("False")