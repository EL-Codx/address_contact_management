from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import UpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# login
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        # authenticating user
        user = authenticate(request, username=username, password=password)
        
        # authorization after authentication and toasting message
        if user is not None:
            messages.success(request, "Login successful")
            login(request, user)
            return redirect("home")
        else:
            messages.success(request, "incorrect username or password")
            return render(request, 'login.html', {})
        
    else:
        return render(request, 'login.html', {})


# logout
def logout_user(request):
    logout(request)
    messages.success(request, "logged out!")
    return render(request, 'login.html', {})


# register
def register_user(request):
    return render(request, 'register.html', {})


# home page
def home(request):
    contacts = Contact.objects.all()
    
    return render(request, 'home.html', {
        "contacts": contacts,
        })


# about page
def about(request):
    return render(request, 'about.html', {})


# individual contact page
def single_contact(request, pk):
    contact = get_object_or_404(Contact, id=pk)
    form = UpdateForm(request.POST or None, request.FILES or None, instance=contact)
    
    # saving form
    if form.is_valid():
        # save the form
        form.save()
        messages.success(request, "The contact has been updated")
        return redirect('home') # redirecting to home
    else:
        render(request, 'contact.html', {"contact": contact, "form": form})
    
    return render(request, 'contact.html', {"contact": contact, "form": form})


# delete 
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, id=pk)
    contact_name = f"{contact.first_name} {contact.last_name}"
    contact.delete() # deleting selected contact
    messages.success(request, f"{contact_name} has been deleted successfully")
    return redirect('home')


# add contact
def add_contact(request):
    form = UpdateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "New record has been added")
        return redirect('home')
    else:
        render(request, 'add_contact.html', {'form': form})
    return render(request, 'add_contact.html', {'form': form})

