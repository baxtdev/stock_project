from django.urls import path
from .views import ProductListView,ProductDetailView,ProductCreateView, ProductUpdateView, ProductDeleteView,export_products_to_excel,\
delete_photo

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('export/', export_products_to_excel, name='export_products_to_excel'),
    path('delete-photo/<int:photo_id>/', delete_photo, name='delete_photo'),
]
