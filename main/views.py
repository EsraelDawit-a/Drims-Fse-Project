from django.db.models import query
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.urls import reverse,reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators import *
from main.models import *
from .forms import *
from main.mixins import *
from management.models import *
from test2.notification import *
from rest_framework import viewsets
from .serializers import *
from main import serializers

''' Api Serilizers '''
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSeliazers

class WantedProductViewSet(viewsets.ModelViewSet):
    queryset = WantedProducts.objects.all()
    serializer_class = WantedProductSerializer


class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transports.objects.all()
    serializer_class = TransportSerialaizer

class TransportOrderViewSet(viewsets.ModelViewSet):
    queryset = TransportOrders.objects.all()
    serializer_class = TransportOrderSerializer


class ProductPriceViewSet(viewsets.ModelViewSet):
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer
''' End Seriizers '''

# Create your views here.
def about_us(request):
    context = {}
    return render(request,'about.html',context)

class CustomUserView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['phone','username','first_name','last_name','Email_Adress','role' ]
    template_name = 'home.html'
    success_url = reverse_lazy('profile_detail')
   
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.kwargs['pk'] = request.user.pk
   



class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profile_details.html'
    context_name = 'detail'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.kwargs['pk'] = request.user.pk

        
def index(request):
    context ={}

    return render(request,'mainhompage.html',context)
        

def resetoptions(request):
    context ={}
    return render(request,'resetoptions.html',context)
    
def registercustomer(request):
    
    form = customerRegister()
    context = {'form1':form}
    if request.method == 'POST':
        form= customerRegister(request.POST or None)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            username = form.cleaned_data.get('username')
            Email= form.cleaned_data.get('Email_Adress')
            phone = formated_number(phone)

            if CustomUser.objects.filter(phone = phone).count()<1:
                request.session['phone'] = phone
                user = form.save(commit =False)
                user.phone = phone
                if Email:
                   user.email = Email
                user.save()
                Profile.objects.create(user=user)
        

                return redirect('vertifyaccount')
            else:
                messages.success(request, 'User With That Phone Number Already Exists ! ')
                return render(request,'register.html',context)
        else:
            print(form.errors)
            print('Not Registerd')
            return render(request,'register.html',context)



    return render(request,'register.html',context)

role = {
    0:'Not set Yet',
    1:'You are Registerd as Buyer',
    2:'You are Registered as Producer',
    3:'You are Registered as Transporter'

}




def vertifyaccount(request):
   form  = VertifyUser(request.POST)
   phone = request.session.get('phone')
   print(phone)
   print(request.session.get('user'))

   user = CustomUser.objects.get(phone=phone)
   if request.method =='POST':
       if form.is_valid():
         num = form.cleaned_data.get('for_m')
         if verify_code(phone,num):
             user.phone_vertified = True
             messages.success(request, 'You Have Sucessusfully Vertified Your Account ')
             user.save()      
             return redirect('loginuser')
         else:
             messages.success(request, 'Incorrect Vertification Code Try Again ')
             return render(request,'vertify.html',context = {'form':form})
   else:
        send_verification(phone)
        return render(request,'vertify.html',context = {'form':form})


def login_view(request):
      form = AuthenticationForm(data=request.POST)
      context = {'form':form}
      if request.method =='POST':
        if form.is_valid():
            print('loged in')
            user = form.get_user()
            if user.is_active == True:
                login(request,user)
                return redirect('homepage')
            else:
                messages.error(request,"You Have Been Restricted From Usingour Serveice Due to UnUsuall activity Try After Some Time! You can Contact us for more info")
                return redirect('loginuser')
            #profile = request.user.prof.get_queryset()
            # customer  = form.cleaned_data['username']
        #    ? values = user.objects.filter(username=customer)     
        else:
            form = AuthenticationForm()
            messages.error(request,"Inccorrect Username Or Password Please Try Again! or You are Currentlly Banned")
            return redirect('loginuser')
      return render(request,'login.html',context)

@login_required
def logoutuser(request):
    # if request.method =="POST":
        logout(request)
        return redirect('loginuser')
    # return render(request,'cheak.html',{'h':45})



@login_required
def search_item(request):
    query = request.GET['query']
    filter_by = request.GET['filter_by']
    if filter_by == 'description':
        product = Products.objects.filter(description__icontains = query)
        paginator = Paginator(product,4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        messages.success(request, 'Your Search Result Here .. ')

        return render(request,'serched_items.html',context={'page_obj':page_obj})

    if filter_by == 'specific_adress':
        product = Products.objects.filter(specific_adress__icontains = query)
        paginator = Paginator(product,4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        messages.success(request, 'Your Search Result Here .. ')

        return render(request,'serched_items.html',context={'page_obj':page_obj})
    
    if filter_by == 'specific_adress':
        product = Products.objects.filter(specific_adress__icontains = query)
        paginator = Paginator(product,4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        messages.success(request, 'Your Search Result Here .. ')
        return render(request,'serched_items.html',context={'page_obj':page_obj})

    
    
    if filter_by == 'product_name':
        product = Products.objects.filter(product_name__icontains = query)
        paginator = Paginator(product,4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        messages.success(request, 'Your Search Result Here .. ')

        return render(request,'serched_items.html',context={'page_obj':page_obj})

    if filter_by == 'price':
        product = Products.objects.filter(price__icontains = query)
        paginator = Paginator(product,4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request,'serched_items.html',context={'page_obj':page_obj})
    
    if filter_by == 'amount':
        product = Products.objects.filter(amount__icontains = query)
        paginator = Paginator(product,4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        messages.success(request, 'Your Search Result Here .. ')

        return render(request,'serched_items.html',context={'page_obj':page_obj})
    


    
    


    


def homepage(request):
            #print(form.cleaned_data['username'])
            farm_stock = Products.objects.filter(catagory__name='Farm stock')
            fashion = Products.objects.filter(catagory__name='Fashion')
            electronics = Products.objects.filter(catagory__name='Electronics')
            other = Products.objects.filter(catagory__name='other')

            

            return render(request,'products.html',{'other':other,'farm_stock':farm_stock,'fashion':fashion,'electronics':electronics})
                 #cheak.html ---befor

@login_required
def productlist(request):
            ob  = Products.objects.all()
            paginator = Paginator(ob,4)
            print(paginator)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request,'productlist.html',context={'page_obj':page_obj})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form1 = CustomerUpdate(request.POST,instance = request.user)
        form2 = ProfUpdate(request.POST,files=request.FILES ,instance = request.user.profile)

        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
           
            print('Profile Updated')
            return redirect('profile_detail')
        else:
             print(form1.errors)
             print(form2.errors)
             form1 = CustomerUpdate(instance = request.user)
             form2 = ProfUpdate(instance = request.user)

             context = {'form1':form1,'form2':form2}

        return render(request,'home.html',context)
    else:
        form1 = CustomerUpdate(instance = request.user)
        form2 = ProfUpdate(instance = request.user)

        context = {'form1':form1,'form2':form2}

        return render(request,'home.html',context)




