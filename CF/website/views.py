from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import record2
from .models import record5
from .models import price
from .models import relation
from .forms import sign_up
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse


global overallnames
overallnames = set()
overallnames.add('admin')



def home(request):
	if request.user.is_authenticated:
		username = request.user.username
		objects = record2.objects.all()
		place = ''
		for item in objects:
			if item.username == username:
				place = item.role

		if place == 'DONOR':
			return render(request,'home.html',{'role' : place})
		if place == 'GRASSROOT WORKER':
			return render(request,'leef.html',{'role' : place})

	return redirect('login')		
	

def user_login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		objects = record2.objects.all()
		place = ''
		for item in objects:
			if item.username == username:
				place = item.role
		user=authenticate(request,username=username,password=password)
		if user:
			login(request,user)

			if place == 'DONOR':
				return redirect('home')
			if place == 'GRASSROOT WORKER':
				return redirect('home')
			if place == "":
				return user_logout(request)
		
	return render(request,'login.html',{})

def user_logout(request):
	logout(request)
	return redirect('truehome')


def studentregister(request):
	if request.user.is_authenticated:
		return render(request,'studentreport.html',{})
	return redirect('login')

def apple(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			name = request.POST['name']
			amount = request.POST['amount']
			quest = price(name = name, amount = amount)
			quest.save()
		return render(request,'apple.html',{})
	return redirect('login')

def children(request):
	if request.user.is_authenticated:
		
		data = [item for item in price.objects.all()]
		return render(request,'childrendata.html',{'data':data})	
	return redirect('login')

def apple(request): 
	if request.user.is_authenticated:

		if request.method=='POST':
			student = request.POST['name']
			donator = request.POST['amount']
			quest = price(name = student, amount = donator)
			quest.save()
			messages.success(request,student+donator)
		return render(request,'apple.html',{})
	return redirect('login')




def register(request):
	if request.method=='POST':
		form=sign_up(request.POST)
		name = request.POST['username']
		role = request.POST['role']
		if name not in overallnames:
			member = record2(username = name,role= role)
		else:
			messages.success(request,'Username already Used')
			return redirect('register')	
			
		if form.is_valid():
			overallnames.add(name)
			form.save()
			member.save()
			messages.success(request,'User Created Succesfully...')
			return redirect('login')
		else:
			messages.success(request,'form invalid')
			
	else:
		form=sign_up()

	return render(request,'register.html',{'form':form})

def sponsor(request):
	if request.user.is_authenticated:
		if request.method=='POST':

			name = request.POST['name']
			email = request.POST['email']
			child = request.POST['child']
			amount = request.POST['amount']
			member = record5(child = child , username = email,amount= amount, name=name)
			member.save()
			relationship = relation(donator = email, student=child)
			relationship.save()
			return render(request,'done.html',{'child': child, 'name':name,'email':email,'amount':amount})
		return render(request,'sponsor.html')
	else:
		return redirect('login')

def truehome(request):
	return render(request,'truehome.html')

def history(request):
	if request.user.is_authenticated:
		name = request.user.username
		data = [item for item in record5.objects.all() if item.username==request.user.username]
		return render(request,'history.html',{'name' : name , 'data':data})

	return redirect('login')

def cloths(request):
	if request.user.is_authenticated:
		return render(request,'cloths.html')
	return redirect('login')


@csrf_protect
def banana(request): #registering
    if request.method == "POST":
        # Get data from the form
        name = request.POST['name']
        sname = request.POST['sname']
        grade = request.POST['grade']
        student_id = request.POST['ID']
        percentage = request.POST['percentage']
        remarks = request.POST['remarks']
        extracurriculars = request.POST['curriculars']

        # Create a session to store the message
        request.session['message'] = f"Student Name: {name}\nSchool Name: {sname}\nGrade: {grade}\nStudent ID: {student_id}\nPercentage: {percentage}\nRemarks: {remarks}\nExtracurriculars: {extracurriculars}"
        
        return redirect('send_email')  # Redirect to the send_email view
    
    return render(request, 'banana.html')

@csrf_protect
def send_email(request):
    if request.method == "POST":
        subject = request.POST['subject']
        message = request.POST['message']
        recipient = request.POST['recipient']
        
        # Send the email
        send_mail(subject, message, 'from@example.com', [recipient])
        
        return HttpResponse('Email sent successfully')
    
    # Pre-fill the message from the session
    message = request.session.get('message', '')
    
    return render(request, 'send_email.html', {'message': message})



def apple(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            student = request.POST.get('name')
            donator = request.POST.get('amount')
            
            if student is not None and donator is not None:
                quest = price(name=student, amount=donator)
                quest.save()
                return render(request, 'apple.html', {'message': 'Data saved successfully.'})
            else:
                return render(request, 'apple.html', {'error': 'Name or amount not provided.'})
        
        return render(request, 'apple.html')
    
    return redirect('login')
