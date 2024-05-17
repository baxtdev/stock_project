from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from .models import Stock, Category, Product, ProductPhoto
from django.utils import timezone

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from .models import ProductPhoto

from django.http import HttpRequest, HttpResponse
from openpyxl import Workbook

class ProductCreateView(CreateView):
    model = Product
    success_url = '/products/'
    fields = ['name', 'description', 'price', 'category']
    template_name = 'product_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        photos = self.request.FILES.getlist('photos')
        for photo in photos:
            ProductPhoto.objects.create(product=self.object, image=photo)
        return response


class ProductDetailView(DetailView):
    model = Product  
    template_name = 'product_view.html'  
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = Product
    success_url = '/products/'
    fields = ['name', 'description', 'price', 'category']
    template_name = 'product_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        photos = self.request.FILES.getlist('photos')
        print(photos)
        for photo in photos:
            ProductPhoto.objects.create(product=self.object, image=photo)
        return response


class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/products/'
    template_name = 'product_confirm_delete.html'


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_queryset(self):
        category_id = self.request.GET.get('category')
        if category_id:
            return Product.objects.filter(category_id=category_id)
        else:
            return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    



def export_products_to_excel(request):
    wb = Workbook()
    ws = wb.active
    ws.append(['id','Name', 'Description', 'Price','created_at'])

    products = Product.objects.all()

    for product in products:
        created_at_str = product.created_at.strftime('%Y-%m-%d %H:%M:%S')
        ws.append([product.id,product.name, product.description, product.price,created_at_str])

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=products.xlsx'

    wb.save(response)
    return response



@require_POST
def delete_photo(request, photo_id):
    photo = get_object_or_404(ProductPhoto, id=photo_id)
    photo.delete()
    return JsonResponse({'status': 'ok'})