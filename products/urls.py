from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('product/<int:product_id>', views.product, name='product'),
    path('product/upvote/<int:product_id>', views.product, name='upvote')
]