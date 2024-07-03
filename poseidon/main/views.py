from django.db.models.query import QuerySet
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import View, ListView
from django.contrib.contenttypes.models import ContentType

from .forms import RegisterForm, LoginForm, CustomUserChangeForm
from .models import Product, Promotion, Entertainment, Service, Visit, Video


User = get_user_model()


class MainView(View):

    def get(self, request):
        context = {
            'products': Product.objects.all()[:5],
            'promotions': Promotion.objects.all(),
            'entertaiments': Entertainment.objects.all(),
            'services': Service.objects.all(),
            'video': Video.objects.first()
        }

        return render(request, 'main/index.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('main:home')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            print(f'valid form: {form.cleaned_data}')
            user = form.get_user()
            login(request, user)
            return redirect('main:home')
        else:
            print(f'{form.errors}, {form.data}')
            return render(request, 'main/login.html', {'form': form})
    else:
        return render(request, 'main/login.html', {'form': LoginForm()})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:home')  # Redirect to a home page or any other page after successful registration
    else:
        form = RegisterForm()

    return render(request, 'main/register.html', {'form': form})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'main/user_page.html'
    success_url = reverse_lazy('main:user_page')

    def get_object(self):
        return self.request.user


def catalog(request):
    context = {
        'products': Product.objects.all()[:5],
        'promotions': Promotion.objects.all(),
        'entertaiments': Entertainment.objects.all(),
        'services': Service.objects.all(),
    }

    return render(request, 'main/catalog.html', context=context)


class VisitsView(ListView):
    context_object_name = 'visits'
    model = Visit
    template_name = 'main/visits.html'


class PromotionsView(ListView):
    template_name = 'main/promotions.html'
    context_object_name = 'promotions'
    model = Promotion


def search_view(request):
    query = request.GET.get('q')
    print(query)
    products = Product.objects.filter(name__regex=r'(?i){}'.format(query)) if query else []
    promotions = Promotion.objects.filter(name__regex=r'(?i){}'.format(query)) if query else []
    entertainment = Entertainment.objects.filter(name__regex=r'(?i){}'.format(query)) if query else []
    service = Service.objects.filter(name__regex=r'(?i){}'.format(query)) if query else []

    context = {
        'products': products,
        'promotions': promotions,
        'entertainment': entertainment,
        'service': service
    }

    return render(request, 'main/search_result.html', context=context)


def create_visit_view(request, pk: int, model: str):
    if request.user.is_authenticated:
        content_type = ContentType.objects.get(app_label='main', model=model)
        content_object = content_type.get_object_for_this_type(pk=pk)
        
        new_visit = Visit(user=request.user)
    
        if model == 'service':
            new_visit.service = content_object
        elif model == 'entertainment':
            new_visit.entertainment = content_object
        elif model == 'promotion':
            new_visit.promotion = content_object
        elif model == 'product':
            new_visit.product = content_object

        new_visit.save()

        return redirect('main:visits')
    else:
        return redirect('main:login')