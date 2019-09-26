import sqlite3
from django.shortcuts import render, redirect, reverse
from hrapp.models import Training_Program
from hrapp.views import *
# from django.contrib.auth.decorators import login_required
from ..connection import Connection

# @login_required
def past_training(request):
    if request.method == 'GET':
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
            where t.start_date < date('now')
            """)

            all_programs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                training = Training_Program()
                training.id = row['id']
                training.title = row['title']
                training.start_date = row['start_date']
                training.end_date = row['end_date']
                training.capacity = row['capacity']
                training.description = row['description']

                all_programs.append(training)

        template = 'training/past_training.html'
        context = {
            'training': all_programs
        }

        return render(request, template, context)
