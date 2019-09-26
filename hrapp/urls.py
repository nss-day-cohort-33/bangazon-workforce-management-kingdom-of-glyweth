from django.urls import path
from django.conf.urls import url, include
from hrapp import views
from .views import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('logout/', logout_user, name='logout'),

    path('departments/', department_list, name='departments'),
    path('departments/form', department_form, name='department_form'),
    path('departments/<int:department_id>', department_details, name='department'),

    path('employees/', employee_list, name='employee_list'),
    path('employees/<int:employee_id>', employee_list, name='employee_list'),
    path('computers/', computer_list, name='computers'),
    # path('computers/<int:computer_id>', computer_list, name='computer'),
    path('computers/<int:computer_id>', computer_details, name='computer'),
    path('computers/form', computer_form, name='computer_form'),

    # path('training/<int:training_program_id>/', training_details, name='training'),
    path('training/', training_list, name='training_list'),
    path('training/past/', past_training, name='past_training'),
    path('training/form', training_form, name='training_form'),
    path('training/<int:training_id>/', training_details, name='training'),
    url(r'^training/(?P<training_id>[0-9]+)/form$', training_edit_form, name='training_edit_form'),
]
