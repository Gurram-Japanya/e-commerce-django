# """
# URL configuration for ecommerce project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """

# from django.contrib import admin
# from django.urls import path
# from .views import (
#     ItemDetailView,
#     HomeView,
#     add_to_cart,
#     remove_from_cart,
#     ShopView,
#     OrderSummaryView,
#     remove_single_item_from_cart,
#     CheckoutView,
#     PaymentView,
#     AddCouponView,
#     RequestRefundView,
#     CategoryView
# )

# app_name = 'core'

# urlpatterns = [
#     path('', HomeView.as_view(), name='home'),
#     path('checkout/', CheckoutView.as_view(), name='checkout'),
#     path('category/<slug>/', CategoryView.as_view(), name='category'),
#     path('product/<slug>/', ItemDetailView.as_view(), name='product'),
#     path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
#     path('add_coupon/', AddCouponView.as_view(), name='add-coupon'),
#     path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
#     path('shop/', ShopView.as_view(), name='shop'),
#     path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
#     path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
#          name='remove-single-item-from-cart'),
#     path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
#     path('request-refund/', RequestRefundView.as_view(), name='request-refund')
#]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)