import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from hrapp.models import Department
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

        return db_cursor.fetchone()


        # all_departments = []
        #     dataset = db_cursor.fetchall()

        #     for row in dataset:
        #         dep = Department()
        #         dep.id = row["id"]
        #         dep.employee_count = row["employee_count"]
        #         dep.name = row["name"]
        #         dep.budget = row["budget"]

        #         all_departments.append(dep)
    #MELANIE! Don't panic... you need to figure out whether you want to get all the employees
    # or just get one table that is for the one department ID.
    #In the SQL call, when I specified "1" as the dep.id, it showed me a table of all the employees
    # that go with dep.id = 1.
    #So this SQL call is bringing in more than one value but it is still only fetching the ID of
    # one department.
    #I may need advice from Stack Overflow or from Joe and Steve...

# @login_required
def department_details(request, department_id):
    if request.method == 'GET':
        department = get_department(department_id)

        template = 'departments/details.html'
        context = {
            'department': department
        }

        return render(request, template, context)

    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM hrapp_department
                WHERE id = ?
                """, (department_id,))

            return redirect(reverse('hrapp:departments'))