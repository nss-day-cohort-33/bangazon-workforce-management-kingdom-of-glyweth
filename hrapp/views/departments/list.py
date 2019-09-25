import sqlite3
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from hrapp.models import Department
from hrapp.models import Employee
from ..connection import Connection

# @login_required
def department_list(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                count(department_id),
                dep.name,
                dep.budget
            from hrapp_employee emp
            inner join hrapp_department dep
            on emp.department_id = dep.id
            group by department_id
            """)

            all_departments = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                dep = Department()
                emp = Employee()
                dep.id = row["id"]
                dep.name = row["name"]
                dep.budget = row["budget"]
                emp.department_id = row["department_id"]

                all_departments.append(dep)
                all_departments.append(emp)

        template_name = 'departments/list.html'

        context = {
            'all_departments': all_departments
        }

        return render(request, template_name, context)