from django.shortcuts import render, redirect 
from datetime import date, datetime
from time import gmtime, strftime
import time
    

def index(request):
    Time=datetime.now().time()
    Today = date.today() 
    context = {
        "time": Time,
        "today":Today
    }
    return render(request,'index.html', context)