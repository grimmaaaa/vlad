from django.urls import path

from .views import *


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('profile/', UserUpdateView.as_view(), name='user_page'),
    path('catalog/', catalog, name='catalog'),
    path('visits/', VisitsView.as_view(), name='visits'),
    path('promotions', PromotionsView.as_view(), name='promotions'),
    path('search/', search_view, name='search'),
    path('create-visit/<int:pk>/<str:model>/', create_visit_view, name='create_visit'),
    path('', MainView.as_view(), name='home'),
]

app_name = 'main'
