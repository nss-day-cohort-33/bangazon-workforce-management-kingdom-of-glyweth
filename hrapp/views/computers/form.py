import sqlite3
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from hrapp.models import Computer
from hrapp.models import employee
from ..connection import Connection


def get_employees():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
        e.id,
            e.first_name,
            e.last_name,
            d.name
        from hrapp_employee e
        join hrapp_department d on e.department_id = d.id;
        """)

        return db_cursor.fetchall()


@login_required
def computer_form(request):
    if request.method == "GET":
        employees = get_employees()
        template = 'computers/form.html'
        context = {
            'employees': employees
        }
        return render(request, template, context)
