from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.conf import settings


from .models import Car
# Create your views here.
def charts(request):
	context={}
	return redirect(request, 'home/highchart.html', context)



def addcar(request, carid = 0):

	if request.method == 'POST' and request.FILES['carimage']:
		carname = request.POST["name"]
		msi = request.POST["msi"]
		price = request.POST["price"]
		capacity  = request.POST["capacity"]
		aircondition  = request.POST["aircondition"]
		transmission  = request.POST["transmission"]
		description  = request.POST["description"]
		carimage = request.FILES['carimage']
		fs = FileSystemStorage()
		filename = fs.save(carimage.name, carimage)
		carimagename = fs.url(filename)

		carObject = Car()
		carObject.name = carname
		carObject.msi = msi
		carObject.description = description
		carObject.price = price
		carObject.capacity = capacity
		carObject.aircondition = aircondition
		carObject.transmission = transmission
		carObject.carimage = carimagename

		carObject.save()



	context = {}

	if carid > 0:
		editCarObject  = Car.objects.get(id=carid)
		context = {'editCarObject':editCarObject}

	
	return redirect(request, 'adminstrator/addcar.html', context)





def icons(request):
	context={}
	return redirect(request, 'adminstrator/icons.html', context)


def dashboard(request):
	context={}
	return redirect(request, 'adminstrator/dashboard.html', context)


def user(request):
	context={}
	return redirect(request, 'adminstrator/user.html', context)

def upgrade(request):
	context={}
	return redirect(request, 'adminstrator/upgrade.html', context)

def carlist(request):
	carList = Car.objects.all().order_by("-id")
	context = {'carLst':carList}
	return redirect(request, 'adminstrator/carlist.html', context)


def table(request):
	context={}
	return redirect(request, 'adminstrator/table.html', context)


def typography(request):
	context={}
	return redirect(request, 'adminstrator/typography.html', context)

def maps(request):
	context={}
	return redirect(request, 'adminstrator/maps.html', context)

def notifications(request):
	context={}
	return redirect(request, 'adminstrator/notifications.html', context)


def deletecar(request, carid):

	Car.objects.filter(id=carid).delete()
	return redirect('/carlist')


def updatecar(request):

	if request.method == 'POST':
		carid = request.POST["hdnCarId"]
		carname = request.POST["name"]
		msi = request.POST["msi"]
		price = request.POST["price"]
		capacity  = request.POST["capacity"]
		aircondition  = request.POST["aircondition"]
		transmission  = request.POST["transmission"]
		description  = request.POST["description"]

		if len(request.FILES) > 0 :
			carimage = request.FILES['carimage']
			fs = FileSystemStorage()
			filename = fs.save(carimage.name, carimage)
			carimagename = fs.url(filename)
		else :
			carimagename = request.POST["hdnImage"]


		updateCarObject = Car.objects.get(id=carid)
		updateCarObject.name = carname
		updateCarObject.msi = msi
		updateCarObject.description = description
		updateCarObject.price = price
		updateCarObject.capacity = capacity
		updateCarObject.aircondition = aircondition
		updateCarObject.transmission = transmission
		updateCarObject.carimage = carimagename

		updateCarObject.save()

	return redirect('/carlist')











