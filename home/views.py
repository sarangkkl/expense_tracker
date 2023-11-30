from django.shortcuts import render,redirect
from home.forms import ExpenseForm, CategoryForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from .models import  Category,Expense
# import sum
from django.db.models import Sum


@login_required(login_url="/login")
def index(request):
    form = ExpenseForm()
    category_form = CategoryForm()
    categories = Category.objects.all()
    expenses = Expense.objects.filter(user=request.user).order_by('-id')
    total_expense = Expense.objects.filter(user=request.user,expense_type='Expense').aggregate(Sum('amount')).get('amount__sum')
    total_earning = Expense.objects.filter(user=request.user,expense_type='Income').aggregate(Sum('amount')).get('amount__sum')
    context = {
        "form":form,
        "category_form":category_form,
        "categories":categories,
        "expenses":expenses,
        "total_expense":total_expense,
        "total_earning":total_earning
    }
    return render(request,"index.html",context)

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect("home")
    else:
        form = CategoryForm()
    
    return redirect("home")
    
def login_handle(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("login")
    else:
        return render(request,"account/login.html")
        
def logout_handle(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect("home")

def handle_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        
        if password != password2:
            messages.error(request,"Passwords do not match")
            return render(request,"account/register.html")
        
        try:
            user = User.objects.create_user(username,email,password,is_active=True)
            user.save()
            messages.success(request,"Successfully Registered")
            return redirect("home")
        except Exception as e:
            messages.error(request,"Username Already Taken",e)
            return redirect("home")
        
    else:
        return render(request,"account/register.html")

@login_required(login_url="/login")
def add_expense(request):
    if request.method == "POST":
        print(request.POST)
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
        
            return redirect("home")
    else:
        pass
    
    return redirect("home")