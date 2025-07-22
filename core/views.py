from django.core.mail import send_mail
from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    message = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment', '')

        # Отправка данных в Google Форму
        form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfg7b4pQAprvKeFIicizS6ITCtySKfkxtns2k-ZXX7otP5hzA/formResponse'
        data = {
            'entry.1725901256': name,      # Имя
            'entry.1030290878': phone,     # Телефон
            'entry.348486074': comment,    # Комментарий
        }
        requests.post(form_url, data=data)

        message = 'Ваша заявка отправлена! Я свяжусь с вами в ближайшее время.'
    return render(request, 'index.html', {'message': message})
