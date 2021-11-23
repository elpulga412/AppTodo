from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *
# Create your views here.
def gallery(request):
    if (request.user.is_authenticated):
        customer = Customer.objects.get(user=request.user)
        print(customer)
        categories = customer.category_set.all()
        category = request.GET.get('category')
        if category == None:
            photos = Photo.objects.filter(category__customer = customer)
        else:
            photos = Photo.objects.filter(category__name = category)
    else:
        categories = Category.objects.all()
        photos = Photo.objects.all()
    context = {'categories': categories, 'photos':photos}
    return render(request, "photoshare/gallery.html", context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {'photo': photo}
    return render(request, "photoshare/photo.html", context)


def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("login ok")
            return redirect('gallery')

    context = {'page':page}
    return render(request, 'photoshare/login_register.html', context)


def registerPage(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        customer = request.POST['username']
        print(customer)
        if form.is_valid():
            print('OK')
            user = form.save(commit=False)
            user.save()
            Customer.objects.create(user=user)
            if user is not None:
                login(request, user)
                return redirect('gallery')
           
    context = {'form':form, 'page': page}
    return render(request, 'photoshare/login_register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('gallery')


def addPhoto(request):
    if request.user.is_authenticated:
        user = request.user
        customer = Customer.objects.get(user=user)
        categories = customer.category_set.all()
        if request.method == 'POST':
            data = request.POST
            images = request.FILES.getlist('images')
            print(images)
            if data['category'] != 'none':
                category = Category.objects.get(name=data['category'])
            elif data['category_new'] != '':
                category, created = Category.objects.get_or_create(
                    customer = customer,
                    name = data['category_new']
                )
                print('Category_customer:',category.customer)
            else:
                category = None
            
            for image in images:
                Photo.objects.create(
                    category = category,
                    image = image,
                    description = data['description']
                )
            return redirect('gallery')
    context = {'categories': categories}
    return render(request, 'photoshare/add.html', context)