from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages






# login
def log_in(request):

    if request.method == "POST":
        user_name = request.POST.get('username')
        print(user_name)
        user_password = request.POST.get('userpassword')
        print(user_password)
        
        user_click=authenticate(request,username=user_name,password=user_password)
        print(user_click)

        if user_click is not None:
            login(request,user_click)
        
            if user_click.is_staff:
                return redirect('list')
                
       
        else:
            messages.info(request,'invalid username and password')
    return render(request,"home.html")



# logout
def log_out(request):
    logout(request)
    return redirect('home')