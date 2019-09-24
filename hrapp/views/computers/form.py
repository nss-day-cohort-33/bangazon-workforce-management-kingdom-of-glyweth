# import sqlite3
# from django.shortcuts import render
# from django.shortcuts import redirect
# from django.urls import reverse
# from hrapp.models import Computer
# from ..connection import Connection

# def computer_list(request):
#     # if request.method == "GET":
#         with sqlite3.connect(Connection.db_path) as conn:
#             conn.row_factory = sqlite3.Row
#             db_cursor = conn.cursor()