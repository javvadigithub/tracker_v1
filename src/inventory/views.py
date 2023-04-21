from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/auth/login')
def index(request):
    return render (request, 'inventory/index.html')

def add_expense(request):
    return render(request, 'inventory/add_expense.html')

