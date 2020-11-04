import mysql.connector
from django.shortcuts import render



def login(request):
    val=request.GET['username']
    val2=request.GET['password']


