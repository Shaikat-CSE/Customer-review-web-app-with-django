from django.urls import path
from .views import product_list, product_review, review_thanks, review_analytics, add_product

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:product_id>/', product_review, name='product_review'),
    path('thanks/', review_thanks, name='review_thanks'),
    path('analytics/', review_analytics, name='review_analytics'),
    path('add_product/', add_product, name='add_product'),
]
