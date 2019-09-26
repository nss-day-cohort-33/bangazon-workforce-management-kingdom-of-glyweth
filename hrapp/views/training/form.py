import sqlite3
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Training_Program
from .details import get_training
from ..connection import Connection

@login_required
def training_form(request):
    if request.method == 'GET':
        training = get_training()
        template = 'training/form.html'
        context = {
            'training': training
        }
        return render(request, template, context)

# @login_required
def training_edit_form(request, training_id):

    if request.method == 'GET':
        training = get_training(training_id)

        template = 'training/form.html'
        context = {
            'training': training
        }

        return render(request, template, context)
