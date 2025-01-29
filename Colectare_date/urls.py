"""
URL configuration for Colectare_date project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from viewer import views
from viewer.views import SelectProductsView, SelectedProductsView, redirect_after_login
from django.contrib.auth import views as auth_views
from viewer.views import select_products
from viewer.views import selected_products
from viewer.views import save_selected, view_selected
from django.views.generic import RedirectView
from viewer.views import view_results
from viewer.views import incentive_view
from viewer.views import purchase_product
from viewer.views import purchase_history_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='login/', permanent=True)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('produse/', views.lista_produse, name='lista_produse'),
    path('magazine/', views.lista_magazine, name='lista_magazine'),
    # path('select-products/', select_products, name='select_products'),
    path('select-products/', SelectProductsView.as_view(), name='select_products'),
    # path('selected-products/', selected_products, name='selected_products'),
    path('selected-products/', SelectedProductsView.as_view(), name='selected_products'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('operator/', views.operator_view, name='operator-view'),
    path('redirect-after-login/', redirect_after_login, name='redirect-after-login'),
    path('save_selected/', save_selected, name='save_selected'),
    path('view-selected/', view_selected, name='view_selected'),
    path('operator/', views.operator_view, name='operator-view'),  # Adaugă ruta pentru operator_view
    path('save_selected/', save_selected, name='save_selected'),
    path('view-results/', view_results, name='view_results'),
    path('incentives/', views.incentive_view, name='incentive_view'),
    path('purchase/<int:product_id>/', views.purchase_product, name='purchase_product'),
    path('purchase-history/', views.purchase_history_view, name='purchase_history_view'),

]
