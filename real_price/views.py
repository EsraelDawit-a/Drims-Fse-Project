from django.shortcuts import render,redirect
from .models import ProductPrice
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import random
def random_digits(n):
    num = range(0, 10)
    lst = random.sample(num, n)
    x = list(map(str,lst))
    return ''.join(x)

def real_price(request):
        product = ProductPrice.objects.filter(is_accepted = True)
        paginator = Paginator(product,4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        messages.success(request, 'Your Search Result Here .. ')

        return render(request,'price_list.html',context={'page_obj':page_obj})



@login_required
def add_product_price(request):
    md = AddProductCatagory.objects.all()
    catagory = AddCatagorypr()
    if request.method == 'POST':
        form= AddProductPrice(request.POST, request.FILES)
        context ={'form':form,'cat':md}
        if form.is_valid():
            form.save()
            context ={'form':form,'cat':md,'catagory':catagory}
            messages.success(request, 'You Have Sucessfully Added new Product Price')
            return render(request,'product_add_price.html',context)
        else:
            messages.success(request, 'Invalid Information Please Provide Valid Information')
            print(request.user.username)
            print(request.user.id)
            return redirect('add_product_price')


    else:
        form = AddProductPrice()
        context ={'form':form,'cat':md,'catagory':catagory}
        if request.user.role == 'Price_teller':
                return render(request,'product_add_price.html',context)
        else:
            return redirect('homepage')


        
        return render(request,'product_add_price.html',context)
    
    
@login_required
def add_catagory_price(request):
      if request.method == 'POST':
          catagory = AddCatagorypr(request.POST)
          if catagory.is_valid():
              catagory.save()
              messages.success(request, 'New Catagory Added ! ')
              return redirect('add_product_price')
          else:
              messages.success(request, 'Invalid Catagory ! ')
              return redirect('add_product_price')
      else:
         return redirect('add_product_price') 



def search_product_price(request):
    query = request.GET['query']
    filter_by = request.GET['filter_by']
    if filter_by == 'description':
        product = ProductPrice.objects.filter(description__icontains = query)
        paginator = Paginator(product,4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        messages.success(request, 'Your Search Result Here .. ')

        return render(request,'product_price_search.html',context={'page_obj':page_obj})


    
    
    if filter_by == 'product_name':
        product = ProductPrice.objects.filter(product_name__icontains = query)
        paginator = Paginator(product,4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        messages.success(request, 'Your Search Result Here .. ')

        return render(request,'product_price_search.html',context={'page_obj':page_obj})

    if filter_by == 'price':
        product = ProductPrice.objects.filter(price__icontains = query)
        paginator = Paginator(product,4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request,'product_price_search.html',context={'page_obj':page_obj})
    
   
   
# def request_email(request):
#     form = getUserEmail()
#     if request.method == "POST":
#         form = getUserEmail(request.POST)
#         if form.is_valid():
#            num = form.cleaned_data.get('for_m')
#            request.session['email'] = num
#            print("Rquest")
#            return redirect('send_email')
#     context= {'form':form}
#     return render(request,'request_email.html',context)

# def send_email(request):
#     form = VertifyUserEmail()
#     if request.method == "POST":
#         form = VertifyUserEmail(request.POST)
#         if form.is_valid():
#             num = form.cleaned_data.get('for_m')
#             pa = request.session.get('passcode')
#             if pa==num:
#                 print(pa,' ',num)
#             else:
#                 print("not equal",pa,' ',num)


#     else:
#         email = request.session.get('email')
#         pass_code =random_digits(8)
#         request.session['passcode'] = pass_code
#         send_mail("Hello From Drims Team",
#         f"Email is sent From Drims Team  \nTo Vertify Your Email Adress\n Your Code : {pass_code}\n Dont Share This Code To Any One",
#         'With Regards Drims Team',
#         [email],
#         fail_silently = False)
        

#         return render(request,'vertify_email.html',context= {'form':form})
