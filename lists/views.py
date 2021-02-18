from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    if request == 'POST':
        return HttpResponse(request.POST['item_text'])
    return render(request, 'lists/home.html')

