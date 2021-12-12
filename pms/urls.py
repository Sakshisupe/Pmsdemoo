
from django.urls import path, include
from . import views
from .import HodViews, StaffViews, StudentViews


urlpatterns = [
    path('', views.loginpage, name="login"),
    path('moreinfo/',views.moreinfo,name='moreinfo'),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('admin_home/', HodViews.admin_home, name="admin_home"),
    path('add_staff/', HodViews.add_staff, name="add_staff"),
    path('add_staff_save/', HodViews.add_staff_save, name="add_staff_save"),
    path('manage_staff/', HodViews.manage_staff, name="manage_staff"),
    path('edit_staff/<staff_id>/', HodViews.edit_staff, name="edit_staff"),
    path('edit_staff_save/', HodViews.edit_staff_save, name="edit_staff_save"),
    path('delete_staff/<staff_id>/', HodViews.delete_staff, name="delete_staff"),
    path('add_domain/', HodViews.add_domain, name="add_domain"),
    path('add_domain_save/', HodViews.add_domain_save, name="add_domain_save"),
    path('manage_domain/', HodViews.manage_domain, name="manage_domain"),
    path('edit_domain/<domain_id>/', HodViews.edit_domain, name="edit_domain"),
    path('edit_domain_save/', HodViews.edit_domain_save, name="edit_domain_save"),
    path('delete_domain/<domain_id>/', HodViews.delete_domain, name="delete_domain"),
    path('add_student/', HodViews.add_student, name="add_student"),
    path('add_student_save/', HodViews.add_student_save, name="add_student_save"),
    path('edit_student/<student_id>', HodViews.edit_student, name="edit_student"),
    path('edit_student_save/', HodViews.edit_student_save, name="edit_student_save"),
    path('manage_student/', HodViews.manage_student, name="manage_student"),
    path('delete_student/<student_id>/', HodViews.delete_student, name="delete_student"),
    path('check_email_exist/', HodViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', HodViews.check_username_exist, name="check_username_exist"),
    path('admin_profile/', HodViews.admin_profile, name="admin_profile"),
    path('admin_profile_update/', HodViews.admin_profile_update, name="admin_profile_update"),
    path('student_feedback_message/', HodViews.student_feedback_message, name="student_feedback_message"),
    path('student_feedback_message_reply/', HodViews.student_feedback_message_reply, name="student_feedback_message_reply"),



    # URLS for Staff
    path('staff_home/', StaffViews.staff_home, name="staff_home"),
    path('staff_profile/', StaffViews.staff_profile, name="staff_profile"),
    path('staff_profile_update/', StaffViews.staff_profile_update, name="staff_profile_update"),
    path('staff_add_result/', StaffViews.staff_add_result, name="staff_add_result"),
    path('check_project/<project_id>/', StaffViews.check_project, name="check_project"),
    path('check_project_save/<project_id>/', StaffViews.check_project_save, name="check_project_save"),

    # URSL for Student
    path('student_home/', StudentViews.student_home, name="student_home"),
    path('student_profile/', StudentViews.student_profile, name="student_profile"),
    path('student_profile_update/', StudentViews.student_profile_update, name="student_profile_update"),
    path('add_project/', StudentViews.add_project, name="add_project"),
    path('showdomain/', StudentViews.showdomain, name="showdomain"),
    path('student_search/', StudentViews.student_search, name="student_search"),
    path('add_project_save/', StudentViews.add_project_save, name="add_project_save"),
    path('manage_project/', StudentViews.manage_project, name="manage_project"),
    path('edit_project/<project_id>/', StudentViews.edit_project, name="edit_project"),
    path('delete_project/<project_id>/', StudentViews.delete_project, name="delete_project"),
    path('edit_project_save/', StudentViews.edit_project_save, name="edit_project_save"),
    path('domaindetails/<int:domain_id>', StudentViews.domaindetails, name="domaindetails"),
    path('studentfeedback/',StudentViews.studentfeedback,name="studentfeedback"),
    path('student_feedback_save/', StudentViews.student_feedback_save, name="student_feedback_save"),
    path('student_view_result/', StudentViews.student_view_result, name="student_view_result"),
    
]