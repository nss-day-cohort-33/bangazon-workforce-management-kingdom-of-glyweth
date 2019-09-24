import sqlite3
from django.shortcuts import render
from hrapp.models import Employee
from hrapp.models import Department
# from django.contrib.auth.decorators import login_required
from ..connection import Connection

# @login_required
def employee_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                e.id,
                e.first_name,
                e.last_name,
                e.is_supervisor,
                e.department_id,
                d.name
            FROM hrapp_employee e LEFT JOIN hrapp_department d ON e.department_id = d.id;
            """)

            all_employees = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                employee = Employee()
                employee.id = row['id']
                employee.first_name = row['first_name']
                employee.last_name = row['last_name']
                employee.is_supervisor = row['is_supervisor']
                employee.department_id = row['department_id']

                department = Department()
                department.id = row['id']
                department.name = row['name']
                # department.budget = row['budget']

                employee.department = department

                all_employees.append(employee)

    template = 'employees/employees_list.html'
    context = {
        'employees': all_employees
    }

    return render(request, template, context)
