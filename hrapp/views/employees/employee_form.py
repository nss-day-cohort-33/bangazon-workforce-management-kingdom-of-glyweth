import sqlite3
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Employee
from ..connection import Connection
from hrapp.views.departments.form import get_departments


def get_employee():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select
                e.id,
                e.first_name,
                e.last_name,
                e.is_supervisor,
                e.start_date,
                e.department_id,
                d.name
            FROM hrapp_employee e LEFT JOIN hrapp_department d ON e.department_id = d.id;
            """)

        return db_cursor.fetchall()


@login_required
def employee_form(request):
    if request.method == 'GET':
        departments = get_departments()
        template = 'employees/employee_form.html'
        context = {
            'all_departments': departments
        }
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_employee
            (
                first_name, last_name, is_supervisor, department_id, start_date
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (form_data['first_name'], form_data['last_name'], form_data['is_supervisor'],
            form_data['department_id'], form_data['start_date'])
            )

        return redirect(reverse('hrapp:employees'))
