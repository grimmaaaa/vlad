from django.contrib import admin

from .models import BaseUser, Service, Entertainment, Promotion, Product, Visit, Video


# Настройка административного интерфейса для модели BAseUser
admin.site.register(BaseUser)
admin.site.register(Video)

# Настройка административного интерфейса для модели Service
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    search_fields = ('name',)
    list_filter = ('price',)
    ordering = ('id',)

# Настройка административного интерфейса для модели Entertainment
@admin.register(Entertainment)
class EntertainmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'duration')
    search_fields = ('name',)
    list_filter = ('duration',)
    ordering = ('id',)

# Настройка административного интерфейса для модели Promotion
@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'start_date', 'end_date')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date')
    ordering = ('id',)

# Настройка административного интерфейса для модели Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    search_fields = ('name',)
    list_filter = ('price',)
    ordering = ('id',)

# Настройка административного интерфейса для модели Visit
@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service', 'entertainment', 'promotion', 'product', 'visit_date')
    search_fields = ('service__name', 'entertainment__name', 'promotion__name', 'product__name')
    list_filter = ('visit_date',)
    ordering = ('id',)
