from datetime import datetime
from django.contrib import messages
from django.shortcuts import redirect, render


from travello.models import Destination
from travello.models import Contact
from travello.models import Worker
from travello.models import Book
# Create your views here.


def index(request): 

    dest1 = Destination()
    dest1.name = 'Carpenter'
    dest1.desc = 'door fitting'
    dest1.url = '/carpenter'
    dest1.img = 'https://res.cloudinary.com/urbanclap/image/upload/q_auto,f_auto,fl_progressive:steep,w_532/t_high_res_category/categories/home_screen/carpenter.jpg'
    dest1.price = '900'
    dest1.offer = False
 
    dest2 = Destination()
    dest2.name = 'Electician'
    dest2.desc = 'wiring'
    dest2.url = '/electrician'
    dest2.img = 'https://res.cloudinary.com/urbanclap/image/upload/q_auto,f_auto,fl_progressive:steep,w_532/t_high_res_category/categories/home_screen/electrician.jpg'
    dest2.price = '800'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Plumber'
    dest3.desc = 'tap fitting'
    dest3.url = '/plumber'
    dest3.img = 'https://res.cloudinary.com/urbanclap/image/upload/q_auto,f_auto,fl_progressive:steep,w_532/t_high_res_category/categories/home_screen/plumber.jpg'
    dest3.price = '750'
    dest3.offer = False
    
    dest4 = Destination()
    dest4.name = 'Salon for Men'
    dest4.desc = 'haircut'
    dest4.url = '/salonmen'
    dest4.img = 'https://img.freepik.com/free-photo/side-view-man-getting-new-hairstyle_23-2148242799.jpg?w=360'
    dest4.price = '750'
    dest4.offer = False
    
    dest5 = Destination()
    dest5.name = 'Salon for Women'
    dest5.desc = 'haircut'
    dest5.url = '/salonwomen'
    dest5.img = 'https://thumbs.dreamstime.com/b/beautiful-woman-hair-salon-going-big-curls-mirror-reflection-young-women-discussing-hairstyling-her-hairdresser-50870416.jpg'
    dest5.price = '750'
    dest5.offer = False
    
    dest6 = Destination()
    dest6.name = 'Spa for Women'
    dest6.desc = 'spa'
    dest6.url = '/spawomen'
    dest6.img = 'https://st4.depositphotos.com/6903990/22657/i/1600/depositphotos_226572400-stock-photo-beautiful-woman-relaxing-spa-salon.jpg'
    dest6.price = '750'
    dest6.offer = False

    dests = [dest1, dest2, dest3, dest4, dest5, dest6]

    #dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})
    

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your feedback has been sent!')
    return render(request, 'contact.html')

def worker(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        worker = Worker(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        worker.save()
        messages.success(request, 'Registraion Complete!')
    return render(request, 'worker.html')


def book(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        desc = request.POST.get('desc')
        book = Book(name=name, email=email, phone=phone, address=address, desc=desc, date=datetime.today())
        book.save()
        messages.success(request, 'Booking confirm!')
    return render(request, 'book.html')

def carpenter(request):
    return render(request, 'carpenter.html')

def electrician(request):
    return render(request, 'electrician.html')

def plumber(request):
    return render(request, 'plumber.html')

def salonmen(request):
    return render(request, 'salonmen.html')

def salonwomen(request):
    return render(request, 'salonwomen.html')

def spawomen(request):
    return render(request, 'spawomen.html')





















# def registerasworker(request):
#     if request.method == "POST":
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         profession = request.POST.get('profession')
#         registerasworker = Registerasworker(first_name=first_name, last_name=last_name, username=username, password1=password1, password2=password2, email=email, phone=phone, profession=profession)
#         registerasworker.save()
#         messages.success(request, 'register successfully.')
#     return render(request, 'registerasworker.html')
        # if password1==password2:
        #     if User.objects.filter(username=username).exists():
        #         messages.info(request, 'Username Taken')
        #         return redirect('registerasworker')
        #     elif User.objects.filter(email=email).exists():
        #         messages.info(request, 'Email Taken')
        #         return redirect('registerasworker')
        #     else:
        #         user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name, contact_number=contact_number, profession=profession)
        #         user.save();
        #         print('user created')
        #         return redirect('login')
        # else:
        #     messages.info(request, 'password not matching...')
        #     return redirect('registerasworker')
        # return redirect('/')

