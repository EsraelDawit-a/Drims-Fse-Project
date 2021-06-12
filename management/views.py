from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic import DetailView,DeleteView
from django.urls import reverse_lazy
from test2.notification import send_message
from django.core.paginator import Paginator
from real_price.models import *
from django.core.mail import send_mail

# Create your views here.
@login_required
def add_product(request):
    md = ProductCatagory.objects.all()
    catagory = AddCatagory()
    if request.method == 'POST':
        form= AddProducts(request.POST, request.FILES)
        context ={'form':form,'cat':md}
        if form.is_valid():
            form.save()
            context ={'form':form,'cat':md,'catagory':catagory}
            messages.success(request, 'You Have Sucessfully Added new Product ')
            return render(request,'product_add.html',context)
        else:
            print(form.errors)
            context ={'form':form,'cat':md,'catagory':catagory}
            print(request.user.username)
            print(request.user.id)
            return render(request,'product_add.html',context)


    else:
        form = AddProducts()
        context ={'form':form,'cat':md,'catagory':catagory}
        if request.user.role == 'Producer':
                return render(request,'product_add.html',context)
        else:
            return redirect('homepage')


        
        return render(request,'product_add.html',context)


@login_required
def delete_product(request,pk):
    item = Products.objects.get(pk=pk)
    item.delete()
    messages.success(request, 'You Have Sucessfully Deleted A Product ')
    return redirect ('user_products')

@login_required
def update_product(request,pk):
    cat = ProductCatagory.objects.all()
    pro = Products.objects.get(pk=pk)
    if request.method == 'POST':
        form1 = AddProducts(request.POST,request.FILES or None,instance = pro)
        if form1.is_valid():
            form1.save()
            print('Product Updated')
            return redirect('user_products')
        else:
            print(form1.errors)
            form1 = AddProducts(instance = pro)
            context = {'form1':form1,'product':pro,'cat':cat,'pk':pk}

            return render(request,'product_update.html',context)
            print(form1.errors)

        
    else:
        
        pro = Products.objects.get(pk=pk)
        form1 = AddProducts(instance = pro)
        context = {'form1':form1,'product':pro,'cat':cat,'pk':pk}

        return render(request,'product_update.html',context)


@login_required
def update_transport(request,pk):
    pro = Transports.objects.get(pk=pk)
    if request.method == 'POST':
        form1 = AddTransports(request.POST,request.FILES or None,instance = pro)
        if form1.is_valid():
            form1.save()
            print('Transport Updated')
            messages.success(request, 'Transport Updated Sucessfully !')
            return redirect('user_products')
        else:
            print(form1.errors)
            form1 = AddTransports(instance = pro)
            context = {'form1':form1,'product':pro,'pk':pk}

            return render(request,'transport_update.html',context)
            print(form1.errors)

        
    else:
        
        pro = Transports.objects.get(pk=pk)
        form1 = AddTransports(instance = pro)
        context = {'form1':form1,'product':pro,'pk':pk}

        return render(request,'transport_update.html',context)



def contactus(request):
    if request.method == "POST":
        form = MessageSend(request.POST)
        if form.is_valid():
            form.save()
        
            print('saved')
            messages.success(request, 'Your Message Have Been Sucssusfuly Sent ')
            print(messages)
            return redirect('contactus')
        else:
            print('notsaved')
            print(form.errors)
            messages.error(request, 'Your Message Have Not Been Sent  ')
            print(messages)
            form = MessageSend()
            context = {'form':form}
            return render(request,'contact.html',context)

    else:
        form = MessageSend()
        context = {'form':form}
        return render(request,'contact.html',context)


@login_required
def delete_orders(request,pk):
    order = ProductOrders.objects.get(pk=pk)
    order.delete()
    messages.success(request, 'Order Deleted Successfully ')
    return redirect('user_products')

@login_required
def delete_transports(request,pk):
    order = Transports.objects.get(pk=pk)
    order.delete()
    messages.success(request, 'Transport Deleted Successfully')
    return redirect('user_products')

@login_required
def user_products(request):
    my_orders = ProductOrders.objects.filter(ordered_by = request.user)
    my_order = my_orders.count()
    print(request.user.role)
    if request.user.role == 'Producer':
            orders = ProductOrders.objects.filter(prouct_owner = request.user)
            order = orders.count()
            print(orders)
            print(request.user.role)
            print(request.user.role)
            man = request.user
            v = Products.objects.filter(user=man)
            context = {}
            amount = v.count()
            context ={'form':v,'amount':amount,'my_orders':my_orders,'my_order':my_order,'orders':orders,'order':order}
        


            return render(request,'userproducts.html',context)
    
    elif request.user.role == 'Transport-Provider':
            
            t_orders = TransportOrders.objects.filter(transport_owner = request.user)
            t_order = t_orders.count()
           
            man = request.user
            v = Transports.objects.filter(user=man)
            amount = v.count()
            context ={'transport':v,'amount':amount,'t_orders':t_orders,'t_order':t_order,'my_orders':my_orders,'my_order':my_order,}
        


            return render(request,'userproducts.html',context)

    elif  request.user.role == 'Price_teller':
       orders = ProductOrders.objects.filter(ordered_by = request.user)
       price_teller = ProductPrice.objects.filter(user = request.user)
       price_count = price_teller.count()
       order = orders.count()
       context = {'orders':orders,'order':order,'price_teller':price_teller,'price_count':price_count}

       return render(request,'price_teller_orders.html',context)

    elif request.user.role =='Buyer':
       orders = ProductOrders.objects.filter(ordered_by = request.user)
       order = orders.count()
       context = {'orders':orders,'order':order}
       return render(request,'buyer_orders.html',context)


    else:
        return redirect('homepage')


@login_required
def add_catagory(request):
      if request.method == 'POST':
          catagory = AddCatagory(request.POST)
          if catagory.is_valid():
              catagory.save()
              messages.success(request, 'New Catagory Added ! ')
              return redirect('create_product')
          else:
              messages.success(request, 'Invalid Catagory ! ')
              return redirect('create_product')
      else:
         return redirect('create_product')




@login_required
def product_detail(request,pk):
   form1 = CommentRev()
   com  = CustomUser.objects.all()
   item = Products.objects.get(pk=pk)
   print(pk)
   if item.user.Adress:
        m =item.user.Adress.split(',')
        la = m[0]
        lo = m[-2]
   else:
        la = '89.002'
        lo = '42.442'
   commentes = CommentReview.objects.filter(product_id=pk)
   print(commentes)
   if request.method =="POST":
        form = CommentRev(request.POST)
        if form.is_valid():
           print('valid')
           form.save()
           print('saved')
           messages.success(request, 'You Have Sucessfully Commented ')
           return render(request,'product_detail_view.html',context={'item':item,'comment':commentes,'com ':com,'form':form1,'la':la,'lo':lo})
        else:
           messages.success(request, 'Unable To Comment! ')
           return render(request,'product_detail_view.html',context={'item':item,'com ':com,'comment':commentes,'form':form1,'la':la,'lo':lo})

        



   return render(request,'product_detail_view.html',context={'item':item,'com ':com,'comment':commentes,'form':form1,'la':la,'lo':lo})

@login_required
def change_status(request,pk):
    item = ProductOrders.objects.get(pk=pk)
    if item.accecpted:
        item.accecpted = False
        man = request.user.username
        body1 = f'\nDear Customer Sorry Your Product Orderd From {man} is Declined Try another Options \n'\
            f'Product_owener:{item.prouct_owner.username}\n' \
            f'orderd_by :{item.ordered_by.username}\n' \
            f'Ordered Date:{item.order_date}\n'\
            f'Ordere Id:{item.pk}\n'\
            f'Price:{item.ordered_item.price} birr {item.ordered_item.amount} \n'\
            f'Delivery Adress:{request.user.optional_adress}\n'\
            f'ordered_item :{item.ordered_item}\n\n' \
            f'FROM DRIMS TEAM. \nTank You For Using Our Service'
        
        if item.ordered_by.Email_Adress:
            email = item.ordered_by.Email_Adress
            send_mail("Hello From Drims Team",
            body1,
            'With Regards Drims Team',
            [email],
            fail_silently = False)
            print('owener email')
        item.save()
        messages.success(request, 'Request Declined')

        return redirect('user_products')

    else:
        item.accecpted = True
        
        phone = item.ordered_by.phone
        owners_phone = item. prouct_owner.phone
        
        body1 = f'\nDear Customer You Have Sucsessfully Orderd A Product \n'\
            f'Your Request is Accepted \n'\
            f'Product_owener:{item.prouct_owner.username}\n' \
            f'orderd_by :{item.ordered_by.username}\n' \
            f'Ordered Date:{item.order_date}\n'\
            f'Ordere Id:{item.pk}\n'\
            f'Price:{item.ordered_item.price} birr {item.ordered_item.amount} \n'\
            f'Delivery Adress:{request.user.optional_adress}\n'\
            f'ordered_item :{item.ordered_item}\n\n' \
            f'Product_owners Phone Number :{owners_phone}\n\n' \
            f'FROM DRIMS TEAM. \nTank You For Using Our Service'
        man = item.ordered_by.username
        body2 = f'\nDear Customer You Have Sucsessfully Accepted Order from {man} \n'\
            f'Your Accepted Order Request \n'\
            f'Product_owener:{item.prouct_owner.username}\n' \
            f'orderd_by :{item.ordered_by.username}\n' \
            f'Ordered Date:{item.order_date}\n'\
            f'Ordere Id:{item.pk}\n'\
            f'Price:{item.ordered_item.price} birr {item.ordered_item.amount} \n'\
            f'Delivery Adress:{request.user.optional_adress}\n'\
            f'ordered_item :{item.ordered_item}\n\n' \
            f'Orderers Phone Number :{phone}\n\n' \
            f'FROM DRIMS TEAM. \nTank You For Using Our Service'

        if item.ordered_by.Email_Adress:
            email = item.ordered_by.Email_Adress
            print('have orderer email')
            send_mail("Hello From Drims Team",
            body1,
            'With Regards Drims Team',
            [email],
            fail_silently = False)
        if item. prouct_owner.Email_Adress:
            email = item. prouct_owner.Email_Adress
            send_mail("Hello From Drims Team",
            body2,
            'With Regards Drims Team',
            [email],
            fail_silently = False)
            print('owener email')
        
        print(body1)
        print(body2)
        item.save()
    
        messages.success(request, 'You Have Sucessfully Accepted A Product Request You will Get Message Notification Soon ')

        return redirect('user_products')





    return redirect('user_products')

@login_required
def change_status_transport(request,pk):
    item = TransportOrders.objects.get(pk=pk)
    if item.status:
        item.status = False
        man =request.user.username
        body1 = f'\nDear {item.ordered_by} Sorry Your Request To Get Transport acess From {man} is Declined \n'\
            f'Transport owener:{item.transport_owner.username}\n' \
            f'orderd_by :{item.ordered_by.username}\n' \
            f'Ordered Date:{item.order_date}\n'\
            f'Ordere Id:{item.pk}\n'\
            f'Try another Options\n'\
            f'FROM DRIMS TEAM. \nTank You For Using Our Service'
        
        if item.ordered_by.Email_Adress:
            email = item.ordered_by.Email_Adress
            send_mail("Hello From Drims Team",
            body1,
            'With Regards Drims Team',
            [email],
            fail_silently = False)
            print('owener email')


        
        item.save()
        messages.success(request, 'Request Declined')
        return redirect('user_products')
    else:
        item.status = True
        owners_phone = item.transport_owner.phone
        man = request.user.username
        body1 = f'\nDear Your Request To Get Transport access From {man} is Accepted \n'\
            f'Your Request is Accepted \n'\
            f'Transport owener:{item.transport_owner.username}\n' \
            f'orderd_by :{item.ordered_by.username}\n' \
            f'Ordered Date:{item.order_date}\n'\
            f'Ordere Id:{item.pk}\n'\
            f'Transport_owners Phone Number :{owners_phone}\n\n' \
            f'FROM DRIMS TEAM. \nTank You For Using Our Service'
        
        if item.ordered_by.Email_Adress:
            email = item.ordered_by.Email_Adress
            send_mail("Hello From Drims Team",
            body1,
            'With Regards Drims Team',
            [email],
            )
            print('owener email')


        send_to = item.ordered_by.phone
        
        print(body1)
        item.save()
        messages.success(request, 'You Have Sucessfully Accepted A Transport Access Request ')

        return redirect('user_products')


@login_required
def order_product(request,pk):
    pro = Products.objects.get(pk=pk)    
    obj = ProductOrders.objects.create(
        ordered_by = request.user,
        order_source_adress = Products.objects.get(pk=pk).user.Adress,
        ordered_item=pro,
        prouct_owner = Products.objects.get(pk=pk).user,
        order_destination = request.user.Adress,
        orderer_optional_adress = request.user.optional_adress
    )

    phone = request.user.phone
    body = f'\nDear Customer You Have Sucsessfully Orderd A Product \n'\
           f'Product_owener:{Products.objects.get(pk=pk).user}\n' \
           f'orderd_by :{request.user}\n' \
           f'Ordered Date:{obj.order_date}\n'\
           f'Price:{pro.price}$ {pro.amount}\n'\
           f'Delivery Adress:{request.user.optional_adress}\n'\
           f'ordered_item :{pro.product_name}\n\n' \
           f'Product_owners Phone Number :{pro.user.phone}\n\n' \
           f'FROM DRIMS TEAM. \nTank You For Using Our Service'

    
   
       
   
    messages.success(request, 'You Have Sucessfully Sent Order Request For Product Owner\n  You will Get Message Notification Soon Wen Request Approved !\n Tank You ! ')

    return redirect('product_detail', pk=pk)



@login_required
def search_transport(request):
    query = request.GET['query']
    filter_by = request.GET['filter_by']
    if filter_by == 'description':
        product = Transports.objects.filter(description__icontains = query)
        paginator = Paginator(product,4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        messages.success(request, 'Your Search Result Here .. ')

        return render(request,'transport_search.html',context={'page_obj':page_obj})

    if filter_by == 'specific_adress':
        product = Transports.objects.filter(specific_adress__icontains = query)
        paginator = Paginator(product,4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        messages.success(request, 'Your Search Result Here .. ')

        return render(request,'transport_search.html',context={'page_obj':page_obj})
    
    

    
    
    if filter_by == 'transport_name':
        product = Transports.objects.filter(transport_name__icontains = query)
        paginator = Paginator(product,4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        messages.success(request, 'Your Search Result Here .. ')

        return render(request,'transport_search.html',context={'page_obj':page_obj})

    if filter_by == 'price':
        product = Transports.objects.filter(price__icontains = query)
        paginator = Paginator(product,4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request,'transport_search.html',context={'page_obj':page_obj})
    
   
   

@login_required
def wantedproductlist(request):
            ob  = WantedProducts.objects.all()
            paginator = Paginator(ob,4)
            print(paginator)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request,'wanted_products_list.html',context={'page_obj':page_obj})

@login_required
def wanted_product_detail(request,pk):
    item = WantedProducts.objects.get(pk=pk)
    if request.method == 'POST':
        phone = item.user.phone
        man =request.user.username
        body = f'\nDear Customer Your Product Have Been Found By {man} \n'\
           f'request id :{item.pk}\n' \
           f'founded By :{request.user}\n' \
           f'request Date:{item.post_date}\n'\
           f'Specific Adress:{item.specific_adress}\n'\
           f'requested_item :{item.product_name}\n\n' \
           f'Founder Phone Number :{request.user.phone}\n\n' \
           f'FROM DRIMS TEAM. \nTank You For Using Our Service'
        messages.success(request, 'Your Request is Sent We Will Get To You Later ! Tankyou')
        print(body)
        return redirect ('wanted_product_detail' ,pk=pk)

    else:
      context ={'item':item}
      return render(request,'wanted_list.html',context)



@login_required
def add_wanted_product(request):
   
    if request.method == 'POST':
        form= AddWantedProducts(request.POST, request.FILES)
        context ={'form':form}
        if form.is_valid():
            form.save()
            context ={'form':form}
            messages.success(request, 'You Have Sucessfully Added Product To Wanted List  ')
            return render(request,'wanted_product.html',context)
        else:
            print(form.errors)
            context ={'form':form}
            print(request.user.username)
            print(request.user.id)
            return render(request,'wanted_product.html',context)


    else:
        form = AddWantedProducts()
        context ={'form':form}


        
        return render(request,'wanted_product.html',context)


@login_required
def transport_add(request):
    form  = AddTransports()
    context = {'form':form}
    if request.method == 'POST':
        form  = AddTransports(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You Have Sucessfully Added Transport Options')
            return redirect('transport_add')
        else:
            messages.success(request, 'You Please Provide Valid Information !!!')
            return redirect('transport_add')
    

    else:
        return render(request,'add_transports.html',context)

@login_required
def display_transports(request):
    ob = Transports.objects.all()
    paginator = Paginator(ob,4)
    print(paginator)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    return render(request,'transport_list.html',context={'page_obj':page_obj})

@login_required
def transport_product_detail(request,pk):
    item = Transports.objects.get(pk=pk)
    if request.method == 'POST':
        print("Request Sent")
        messages.success(request, 'Your Request is Sent We Will Get To You Later ! Tankyou')
        return redirect ('transport_product_detail' ,pk=pk)

    else:
      context ={'item':item}
      return render(request,'transport_details.html',context)


@login_required
def order_Transport(request,pk):
    pro = Transports.objects.get(pk=pk)    
    obj = TransportOrders.objects.create(
        ordered_by = request.user,
        order_source_adress = Transports.objects.get(pk=pk).user.Adress,
        transport_owner = Transports.objects.get(pk=pk).user,
        orderer_optional_adress = request.user.optional_adress
    )


    messages.success(request, 'You Have Sucessfully Requested A Transport Acsess We Will Get \nTo You When Request Is Accpted Tankyou ! ')

    return redirect('transport_product_detail', pk=pk)

