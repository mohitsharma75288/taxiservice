from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.conf import settings


from .models import Car
# Create your views here.

def home(request):
	context = {}
	return render(request, 'home/home.html', context)



def about(request):
	context = {}
	return render(request, 'home/about.html', context)


def gallery(request):
	context = {}
	return render(request, 'home/gallery.html', context)


def contact(request):

	context = {}

	if request.method == 'POST':

		subject = request.POST["subject"]
		message = request.POST["message"]
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [request.POST["email"]]
		#send_mail( subject, message, email_from, recipient_list)
		context = {'message':"We will contact you shortly."}


	return render(request, 'home/contact.html', context)


def service(request):
	context = {}
	return render(request, 'home/service.html', context)


def elements(request):
	context = {}
	return render(request, 'home/elements.html', context)


def cars(request):
	carList = Car.objects.all().order_by("-id")[:3]
	context = {'carLst':carList}
	return render(request, 'home/cars.html', context)


def blog1(request):

	context = {}
	return render(request, 'home/blog1.html', context)


def blog2(request):

	context = {}
	return render(request, 'home/blog2.html', context)




















