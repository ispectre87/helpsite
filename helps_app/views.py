from django.shortcuts import render, redirect
from .models import HelpRequest
from .forms import CteateRequest

def index(request):
    return render(request, 'helps_app/index.html')

def help_requests(request):
    help_title = HelpRequest.objects.all()
    context = {'help_title': help_title}
    return render(request, 'helps_app/help_requests.html', context)

def need_help(request):
    if request.method != 'POST':
        form = CteateRequest()

    else:
        form = CteateRequest(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('helps_app:request_added')
    context = {'form': form}
    return render(request, 'helps_app/need_help.html', context=context)

def help_request_detail(request, title_id):
    help_detail = HelpRequest.objects.get(pk=title_id)
    title = help_detail.title
    text = help_detail.text
    date = help_detail.pub_date
    contacts = help_detail.contacts
    city = help_detail.city
    context = {
        'title': title,
        'city': city,
        'text': text,
        'date': date,
        'contacts': contacts,
        }
    return render(request, 'helps_app/help_request_detail.html', context)

def request_added(request):
    return render(request, 'helps_app/request_added.html')

