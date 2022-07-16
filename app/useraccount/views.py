from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully Logged In')
            return redirect('/')
        else:
            messages.error(request,'invalid username or password!')
            return redirect('login')
    return render(request,"useraccount/login.html")