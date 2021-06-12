from .models import *
from django.forms import *
from django.contrib.auth.forms import UserCreationForm

class customerRegister(UserCreationForm):
    #password1 =forms.CharField(label='Password',widget=forms.PasswordInput())
    #password2 =forms.CharField(label='Password Confirm',widget=forms.PasswordInput())
    class Meta:
        model =  CustomUser
        fields = ['phone','username','first_name','last_name','Email_Adress','role','Adress','optional_adress' ]


class CustomerUpdate(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone','username','first_name','last_name','Email_Adress','role','Adress','optional_adress' ]
    

class ProfUpdate(ModelForm):
    class Meta:
        model = Profile
        fields = ['pic','bio','licencecopy','idimg']

class TrasnsporterData(ModelForm):
    class Meta:
         model = Profile
         fields = ['licencecopy','idimg']



class VertifyUser(forms.Form):
    for_m = CharField(max_length = 6)
    


# class Sellererreg(forms.ModelForm):
#     class Meta:
#         model = Seller
#         fields = ['Adress','pic','bio','docimage','is_premium_account','Sellertype','producttype']




# class Transporterrerreg(forms.ModelForm):
#     class Meta:
#         model = Transporter
#         fields = ['Adress','pic','bio','idimg','Transporter_type','licencecopy']

# class BranchAdminRegistration(UserCreationForm):
#     model = BranchAdminRegistration
#     fields = '__all__'