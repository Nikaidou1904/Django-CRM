from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddAirlineForm, AddBackpackForm
from .models import Record, Airline, Backpack





# Home page
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





# Authentication
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

# This is for the airline table in airline.html
def airline_record(request):
	if request.user.is_authenticated:
		airlines = Airline.objects.all()
		return render(request, 'airline.html', {'airlines':airlines})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')


# For clickable ID in airline.html, which then redirects you to info_airline.html
def info_airline(request, pk):
	if request.user.is_authenticated:
		info_airline = Airline.objects.get(id=pk)
		return render(request, 'info_airline.html', {'info_airline':info_airline})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')


# Delete button in info_airline.html
def delete_airline(request, pk):
	if request.user.is_authenticated:
		delete_it = Airline.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('airline')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


# This is for a URL in the navbar that redirects to the form add_airline.html
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


# Update button in info_airline.html, which then redirects you to update_airline.html
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

# This is for the backpack table in backpack.html
def backpack_record(request):
	if request.user.is_authenticated:
		# For Backpak Page
		backpacks = Backpack.objects.all()
		return render(request, 'backpack.html', {'backpacks':backpacks})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')


# For clickable ID in backpack.html, which then redirects you to info_backpack.html
def info_backpack(request, pk):
	if request.user.is_authenticated:
		# For Each Backpack ID
		info_backpack = Backpack.objects.get(id=pk)
		return render(request, 'info_backpack.html', {'info_backpack':info_backpack})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')


# Delete button in info_backpack.html
def delete_backpack(request, pk):
	if request.user.is_authenticated:
		delete_it = Backpack.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('backpack')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


# This is for a URL in the navbar that redirects to the form add_backpack.html
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


# Update button in info_backpack.html, which then redirects you to backpack.html
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