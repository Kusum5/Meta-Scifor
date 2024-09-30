from django.contrib import messages
from django.shortcuts import render
import os
import json
from django.conf import settings
from .models import Preferences

# Create your views here.
def index(request):
    currency_data = []
    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        for k, v in data.items():
            currency_data.append({'name': k, 'value': v})

    exists = Preferences.objects.filter(user=request.user).exists()

    preferences = None
    if exists:
        preferences = Preferences.objects.get(user=request.user)

    if request.method == 'GET':
        return render(request, 'preferences/index.html', {'currencies': currency_data,'preferences':preferences})
    else:
        currency = request.POST['currency']
        if exists:
            preferences.currency = currency
            preferences.save()
        else:
            Preferences.objects.create(user=request.user, currency=currency)

        messages.success(request, 'Changes saved')
        return render(request, 'preferences/index.html',
                      {'currencies': currency_data, 'preferences': preferences})
