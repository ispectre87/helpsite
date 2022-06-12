from django.shortcuts import render, redirect
from .models import HelpRequest, City, Region
from .forms import CteateRequest

def index(request):
    """Главная страница сайта"""
    regions = Region.objects.all()
    context = {
        'regions': regions,
    }
    return render(request, 'helps_app/index.html', context)

def cities(request, region_id):
    """Отображает список городов по региону"""
    cities = City.objects.filter(region_id=region_id)
    context = {
        'cities': cities,
        'region_id': region_id,
    }
    return render(request, 'helps_app/cities.html', context)

def help_requests(request, city_id, region_id):
    """Отображает список заявок по городу"""
    help_title = HelpRequest.objects.filter(citi_name_id=city_id)
    context = {
        'help_title': help_title,
        'city_id': city_id,
    }
    return render(request, 'helps_app/help_requests.html', context)

def need_help(request, city_id):
    """Форма заявки на помощь"""
    if request.method != 'POST':
        form = CteateRequest()
    else:
        form = CteateRequest(data=request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.citi_name_id = city_id
            q.save()
            return redirect('helps_app:request_added')
    context = {'form': form, 'city_id': city_id}
    return render(request, 'helps_app/need_help.html', context=context)

def help_request_detail(request, title_id):
    """Полная информация по заявке"""
    help_detail = HelpRequest.objects.get(pk=title_id)
    title = help_detail.title
    text = help_detail.text
    date = help_detail.pub_date
    contacts = help_detail.contacts
    context = {
        'title': title,
        'text': text,
        'date': date,
        'contacts': contacts,
        }
    return render(request, 'helps_app/help_request_detail.html', context)

def request_added(request):
    return render(request, 'helps_app/request_added.html')

