import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import Training_Program
from ..connection import Connection

@login_required
def training_form(request):
    if request.method == 'GET':
        template = 'training/form.html'
        context = {}

        return render(request, template, context)