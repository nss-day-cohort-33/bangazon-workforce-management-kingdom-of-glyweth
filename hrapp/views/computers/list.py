import sqlite3
from django.shortcuts import render
# from django.shortcuts import redirect
# from django.urls import reverse
from hrapp.models import Computer
from ..connection import Connection

def computer_list(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                c.id,
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
                computer.id = row['id']
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
    elif request.method == 'POST':
        form_data = request.Post

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_computer
            (
                purchase_date, decommission_date, manufacturer, model
            )
            VALUES (?, ?, ?, ?)
            """,
                (form_data['purchase_date'], 