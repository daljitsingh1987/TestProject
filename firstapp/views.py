from django.shortcuts import render,HttpResponse
from firstapp.forms import MySiteUserForm

#Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to First Response</h1>")
def home(request):
    return render(request,"index.html")
def testhome(request):
    return render(request,"home.html")
def testhome2(request):
    return render(request,"testhome2.html")
def signup(request):
    if request.method=="POST":
        form=MySiteUserForm(request.POST)
        f=form.save(commit=False)
        f.userFullName=request.POST["username"]
        f.userEmail = request.POST["useremail"]
        f.userPassword = request.POST["userpassword"]
        f.userMobile = request.POST["usermobile"]
        f.isActive = True
        f.roleId_id=2
        f.save()
        return render(request, "signup.html",{'sucess':True})

    return render(request,"signup.html")