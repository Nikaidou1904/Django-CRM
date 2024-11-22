from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddAirlineForm, AddBackpackForm
from .models import Record, Airline, Backpack





# Home page cuz why not
def home(request):
	records = Record.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':records})





# Authentication stuff
def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



# Airline CRUD
def airline_record(request):
	if request.user.is_authenticated:
		# For Airline Page
		airlines = Airline.objects.all()
		return render(request, 'airline.html', {'airlines':airlines})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



def info_airline(request, pk):
	if request.user.is_authenticated:
		# For Each Airline ID
		info_airline = Airline.objects.get(id=pk)
		return render(request, 'info_airline.html', {'info_airline':info_airline})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



def delete_airline(request, pk):
	if request.user.is_authenticated:
		delete_it = Airline.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('airline')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_airline(request):
	form = AddAirlineForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_airline = form.save()
				messages.success(request, "Record Added...")
				return redirect('airline')
		return render(request, 'add_airline.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_airline(request, pk):
	if request.user.is_authenticated:
		current_record = Airline.objects.get(id=pk)
		form = AddAirlineForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('airline')
		return render(request, 'update_airline.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')





# Backpack CRUD
def backpack_record(request):
	if request.user.is_authenticated:
		# For Backpak Page
		backpacks = Backpack.objects.all()
		return render(request, 'backpack.html', {'backpacks':backpacks})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def info_backpack(request, pk):
	if request.user.is_authenticated:
		# For Each Backpack ID
		info_backpack = Backpack.objects.get(id=pk)
		return render(request, 'info_backpack.html', {'info_backpack':info_backpack})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



def delete_backpack(request, pk):
	if request.user.is_authenticated:
		delete_it = Backpack.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('backpack')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_backpack(request):
	form = AddBackpackForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_backpack = form.save()
				messages.success(request, "Record Added...")
				return redirect('backpack')
		return render(request, 'add_backpack.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')


def update_backpack(request, pk):
	if request.user.is_authenticated:
		current_backpack = Backpack.objects.get(id=pk)
		form = AddBackpackForm(request.POST or None, instance=current_backpack)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('backpack')
		return render(request, 'update_backpack.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')