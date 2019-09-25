import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Training_Program
from ..connection import Connection


def get_training(training_program_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id training_program_id,
            t.title,
            t.start_date,
            t.end_date,
            t.capacity,
            t.description,
        FROM hrapp_training_program t
        WHERE t.id = ?
        """, (training_program_id,))

        return db_cursor.fetchone()

@login_required
def training_details(request, training_program_id):
    if request.method == 'GET':
        training = get_training(training_program_id)

        template = 'training/detail.html'
        context = {
            'training': training
        }

        return render(request, template, context)