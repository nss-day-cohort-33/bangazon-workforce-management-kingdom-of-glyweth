import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Training_Program, model_factory
from ..connection import Connection


def get_training(training_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id training_id,
            t.title,
            t.start_date,
            t.end_date,
            t.capacity,
            t.description
        FROM hrapp_training_program t
        WHERE t.id = ?
        """, (training_id,))

        return db_cursor.fetchone()

@login_required
def training_details(request, training_id):
    if request.method == 'GET':
        training = get_training(training_id)

        template = 'training/detail.html'
        context = {
            'training': training
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE hrapp_training_program
                SET title = ?,
                    start_date = ?,
                    end_date = ?,
                    capacity = ?,
                    description = ?
                WHERE id = ?
                """,
                (
                    form_data['title'], form_data['start_date'],
                    form_data['end_date'], form_data['capacity'],
                    form_data["description"], training_id,
                ))

            return redirect(reverse('hrapp:training'))

        # Check if this POST is for deleting
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM hrapp_training_program
                WHERE id = ?
                """, (training_id,))

            return redirect(reverse('hrapp:training_list'))