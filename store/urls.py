from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.age, name='age_req'),
    path('product_all/', views.product_all, name='product_all'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    path('search/', views.searchBar, name='search'),
    path('deny/', views.deny, name='deny'),
]
