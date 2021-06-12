from django.shortcuts import render,redirect
from .models import Product
from .forms import AddproductForm
from django.contrib import messages

# Create your views here.
def productss(request):
	item = Product.objects.all()

	return render (request,'product.html',context = {'item':item})
def product_add_view(request):
	product_add_form = AddproductForm(request.POST,request.FILES)
	if request.method =='POST':
		if product_add_form.is_valid():
			product_add_form.save()
			print('saved')
			messages.success(request,'Suucessfully Added A product')
			return redirect('product_add_view')
		else:
			print(product_add_form.errors)
			messages.success(request,'Unable TO Create Product')
			return redirect('product_add_view')

	else:
		 product_add_form = AddproductForm()
		 context = {'form':product_add_form}
		 return render(request,'product_add.html',context)