from django.shortcuts import render
from regandloginapp.models import RegistrationData
from regandloginapp.forms import RegistrationForm, LoginForm
from django.http.response import HttpResponse
# from django.contrib import messages

# Create your views here.
# def index(request):
#     return render(request,'index.html')


def registration_view(request):
    if request.method == "POST":
        eform = RegistrationForm(request.POST)
        if eform.is_valid():
            fname = request.POST.get('firstname')
            lname = request.POST.get('lastname')
            uname = request.POST.get('username')
            password = request.POST.get('password')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            gender = eform.cleaned_data.get('gender')
            dob = eform.cleaned_data.get('date_of_birth')
            data  =RegistrationData(
                firstname=fname,
                lastname=lname,
                username=uname,
                password=password,
                mobile=mobile,
                email=email,
                gender=gender,
                date_of_birth=dob
            )
            data.save()
            # messages.success(request,'User registration successfully')
            eform = RegistrationForm()
            return render(request,'registration.html',{'eform':eform})
        else:
         return HttpResponse("User missed data")
    else:
     eform=RegistrationForm()
     return render(request,'registration.html',{'eform':eform})


def login_view(request):
    if request.method=="POST":
        eform = LoginForm(request.POST)
        if eform.is_valid():
            uname = request.POST.get('username')
            pwd = request.POST.get('password')

            uname1=RegistrationData.objects.filter(username=uname,password=pwd)
            # pwd1=RegistrationData.objects.filter(password=pwd)

            if uname1:
                return HttpResponse("Success")
            else:
                return HttpResponse("Invalid credentials")
        else:
            return HttpResponse("user missed value")
    else:
        eform=LoginForm()
        return render(request,'login.html',{'eform':eform})
