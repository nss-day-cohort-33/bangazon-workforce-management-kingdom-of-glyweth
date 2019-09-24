import sqlite3
# from django.urls import reverse
from django.shortcuts import render, redirect
from hrapp.models import Computer
from ..connection import Connection


def get_computer(computer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            c.id
            c.manufacturer,
            c.model,
            c.purchase_date,
            c.decommission_date
        from hrapp_computer c;
        """)

        return db_cursor.fetchone()

def computer_details(request, computer_id):
    if request.method == 'GET':
        computer = get_computer(computer_id)
        template = 'computers/detail.html'
        context = {
            'computer': computer
        }
        return render(request, template, context)


