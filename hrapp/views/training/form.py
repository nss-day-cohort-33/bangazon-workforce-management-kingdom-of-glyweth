import sqlite3
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Training_Program
from ..connection import Connection


def get_training():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select
                t.id,
                t.title,
                t.start_date,
                t.end_date,
                t.capacity,
                t.description
            from hrapp_training_program t
            """)

        return db_cursor.fetchall()

@login_required
def training_form(request):
    if request.method == 'GET':
        training = get_training()
        template = 'training/form.html'
        context = {
            'all_training': training
        }
        return render(request, template, context)
