from django.urls import path
from django.conf.urls import include
from hrapp import views
from .views import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('departments/', department_list, name='departments'),
    path('departments/form', department_form, name='department_form'),
    path('departments/<int:department_id>', department_details, name='department'),
    path('employees/', employee_list, name='employee_list'),

    path('computers/', computer_list, name='computers'),
    path('training_program/', training_list, name='training_list'),
    path('training/form', training_form, name='training_form'),
]
