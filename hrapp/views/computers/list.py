import sqlite3
from django.shortcuts import render
# from django.shortcuts import redirect
# from django.urls import reverse
from hrapp.models import Computer
from ..connection import Connection
# from django.contrib.auth.decorators import login_required

# @login_required
def computer_list(request):
    # if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
				c.manufacturer,
				c.model,
				c.purchase_date,
				c.decommission_date
            from hrapp_computer c
            """)

            all_computers = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                computer = Computer()
                computer.manufacturer = row['manufacturer']
                computer.model = row['model']
                computer.purchase_date = row['purchase_date']
                computer.decommission_date = row['decommission_date']

                all_computers.append(computer)


        template = 'computers/list.html'
        context = {
            'computers': all_computers
        }
        #In DJANGO you have to manually wire up URLs
        return render(request, template, context)