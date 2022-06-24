from django.shortcuts import render, redirect
from .models import HelpRequest, City, Region
from .forms import CreateRequest, UserRegister
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

class HelpHomepage(generic.ListView):
    model = Region                          #модель на основании которой строится список
    template_name = 'helps_app/index.html'  #имя шаблона
    context_object_name = 'regions'         #имя списка в самом шаблоне

    def get_queryset(self):
        return Region.objects.order_by('region_name')

# def index(request):
#     """Главная страница сайта"""
#     regions = Region.objects.all()
#     context = {
#         'regions': regions,
#     }
#     return render(request, 'helps_app/index.html', context)

class CitiesList(generic.ListView):
    model = City
    template_name = 'helps_app/cities.html'
    context_object_name = 'cities'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        helprequests = HelpRequest.objects.filter(citi_name__region_id=self.kwargs['region_id']).order_by('-update')
        paginator = Paginator(helprequests, 20)
        page_number = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page_number)
        context['region'] = Region.objects.get(pk = self.kwargs['region_id'])
        return context

    def get_queryset(self):
        return City.objects.filter(region_id=self.kwargs['region_id'])

# def cities(request, region_id):
#     """Отображает список городов по региону"""
#     cities = City.objects.filter(region_id=region_id)
#     context = {
#         'cities': cities,
#         'region_id': region_id,
#     }
#     return render(request, 'helps_app/cities.html', context)

class HelpRequests(generic.ListView):
    paginate_by = 20
    model = HelpRequest
    template_name = 'helps_app/help_requests.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['city_id'] = self.kwargs['city_id']
        context['city_name'] = City.objects.get(pk=self.kwargs['city_id']).city_name
        return context

    def get_queryset(self):
        return HelpRequest.objects.filter(citi_name_id = self.kwargs['city_id']).order_by('-update')

# def help_requests(request, city_id, region_id):
#     """Отображает список заявок по городу"""
#     help_title = HelpRequest.objects.filter(citi_name_id=city_id)
#     context = {
#         'help_title': help_title,
#         'city_id': city_id,
#     }
#     return render(request, 'helps_app/help_requests.html', context)

# class CreateHelpRequest(generic.CreateView):
"""Не знаю как сделать привязку к городу"""
#     form_class = CreateRequest
#     template_name = 'helps_app/need_help.html'
#     pk_url_kwarg = 'city_id'

@login_required
def need_help(request, city_id):
    """Форма заявки на помощь"""
    if request.method != 'POST':
        form = CreateRequest()
    else:
        form = CreateRequest(data=request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.citi_name_id = city_id
            q.user_id = request.user.id
            q.save()
            return redirect('helps_app:request_added')
    context = {'form': form, 'city_id': city_id}
    return render(request, 'helps_app/need_help.html', context=context)

class HelpRequestDetail(generic.DetailView):
    model = HelpRequest
    template_name = 'helps_app/help_request_detail.html'
    context_object_name = 'request_detail'
    pk_url_kwarg = 'help_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return HelpRequest.objects.filter(pk=self.kwargs['help_id'])

# def help_request_detail(request, help_id):
#     """Полная информация по заявке"""
#     help_detail = HelpRequest.objects.get(pk=help_id)
#     title = help_detail.title
#     text = help_detail.text
#     date = help_detail.pub_date
#     contacts = help_detail.contacts
#     context = {
#         'title': title,
#         'text': text,
#         'date': date,
#         'contacts': contacts,
#         }
#     return render(request, 'helps_app/help_request_detail.html', context)

def request_added(request):
    return render(request, 'helps_app/request_added.html')

class Registration(generic.CreateView):
    """Выводит форму регистрации"""
    form_class = UserRegister
    template_name = 'helps_app/registration.html'
    success_url = reverse_lazy('helps_app:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('helps_app:index')


class LoginUser(LoginView):
    """Форма для входа на сайт"""
    form_class = AuthenticationForm
    template_name = 'helps_app/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('helps_app:index')

def logout_user(request):
    """Деавторизует пользователя, показывает прощальную страницу"""
    logout(request)
    return render(request, 'helps_app/logout.html')

def about(request):
    return render(request, "helps_app/about.html")


