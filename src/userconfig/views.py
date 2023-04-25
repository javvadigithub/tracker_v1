from django.shortcuts import render
import os
import json
from django.conf import settings
from .models import UserConfig
from django.contrib import messages

# Create your views here.

def index(request):
    currency_data = []
    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        for k, v in data.items():
            currency_data.append({'name': k, 'value': v})

    exists = UserConfig.objects.filter(user=request.user).exists()
    user_config = None
    if exists:
        user_config = UserConfig.objects.get(user=request.user)
    if request.method == 'GET':

        return render(request, 'userconfig/index.html', {'currencies': currency_data, 'user_config': user_config})

    else:

        currency = request.POST['currency']
        if exists:
            user_config.currency = currency
            user_config.save()
        else:
            UserConfig.objects.create(user=request.user, currency=currency)
        messages.success(request, 'Changes saved')
        return render(request, 'userconfig/index.html', {'currencies': currency_data, 'user_config': user_config})
