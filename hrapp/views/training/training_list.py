import sqlite3
from django.shortcuts import render
from hrapp.models import Training_Program
from hrapp.views import *


def training_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # TODO: Add to query: e.department,
            db_cursor.execute("""
            select
                t.id,
                t.title,
                t.start_date,
                t.end_date,
                t.capacity
            from hrapp_training_program t
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

                all_programs.append(training)

    template = 'training/training_list.html'
    context = {
        'training': all_programs
    }

    return render(request, template, context)
