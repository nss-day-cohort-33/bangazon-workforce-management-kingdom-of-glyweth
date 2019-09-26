import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from hrapp.models import Department
from hrapp.models import Employee
from ..connection import Connection


def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            dep.id,
            emp.first_name,
            emp.last_name,
            dep.name,
            dep.budget
            from hrapp_employee emp
            join  hrapp_department dep on emp.department_id = dep.id
        WHERE dep.id = ?
        """, (department_id,))

        return db_cursor.fetchall()


def department_details(request, department_id):
    if request.method == 'GET':
        department = get_department(department_id)
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = create_list_employees

        template = 'departments/details.html'
        context = {
            'department': department
        }

        return render(request, template, context)

def create_list_employees(cursor, row):
    _row = sqlite3.Row(cursor, row)

    department = Department()
    department.id = _row["id"]
    department.name = _row["name"]
    department.budget = _row["budget"]

    department.employees = []

    employee = Employee()
    employee.department_id = _row["department_id"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]

    department_employees = {}

    for (department, employee) in department:

        if department.id not in department_employees:
            department_employees[department.id] = department
            department_employees[department.id].employees.append(employee)

        else:
            department_employees[department.id].employees.append(employee)

    return (department, employee,)