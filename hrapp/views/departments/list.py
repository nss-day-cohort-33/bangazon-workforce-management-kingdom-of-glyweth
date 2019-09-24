import sqlite3
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from hrapp.models import Department
from ..connections import Connection

# @login_required
def department_list(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                dep.id,
                dep.name,
                dep.budget
            from hrapp_department dep
            """)

            all_departments = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                dep = Department()
                dep.id = row["id"]
                dep.name = row["name"]
                dep.budget = row["budget"]

                all_departments.append(dep)

        template_name = 'departments/list.html'

        context = {
            'all_departments': all_departments
        }

        return render(request, template_name, context)