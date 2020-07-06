from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.db.models import F
from django.contrib.auth import login, authenticate, logout
from .filters import AstroFilter
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

import stripe

stripe.api_key = ('sk_test_51GzwicFlMZrJNY0xzkbFfyuVlnGK2Fuu77qFgpsCdMjTuDT8aCTeh9bIUxmXMZmFCRSx0WLtnGQb7598hFFXcldp00xF0KKieG')

def astrosearch(request):
	astrologer = Astro_Profile.objects.all()
	
	astro_count = astrologer.count()

	myFilter = AstroFilter(request.GET, queryset=astrologer)
	astrologer = myFilter.qs

	context = { 'astrologer' : astrologer, 'astro_count':astro_count, 'myFilter':myFilter}
	return render(request, 'search.html', context)




def Convert(string):
	li = list(string.split(" "))
	return li

def signup(request):
    if request.method == 'POST':
        form1 = SignupForm(request.POST)
       

        if form1.is_valid():

            user = form1.save(commit=True)
            user.is_active = False
            user.save()

            

            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })

            to_email = Convert(form1.cleaned_data.get('email'))
            print(to_email)
            send_mail('test', message ,'najay357@gmail.com', to_email, fail_silently=False)
            
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form1 = SignupForm()
       
    return render(request, 'signup.html', {'form1': form1})



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        
        pro = user
        user.save()
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")


        return HttpResponse('We have confirmed account,  go to home')


        
    else:
        return HttpResponse('Activation link is invalid!')

# Create your views here.
def index(request):
	astrologer = Astro_Profile.objects.all()
	return render(request,'index.html', {'astrologer':astrologer})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def logout(request):
    return render(request,'logout.html')

def dashboard(request):
    return render(request,'dashboard.html')

def createastroprofile(request):
	prof = request.user.profile
	if request.method == "POST":
		form = AstroProfileForm(request.POST)
		 
		if form.is_valid():
			astro_profile = form.save(commit=False)
			astro_profile.profile = prof
			astro_profile.save()

			
			return redirect(reverse('dashboard'))

	else:
		form = AstroProfileForm()
		

	return render(request, 'astroprofile.html', {'form':form})
	


def completeprofile(request):
	if request.method == "POST":
		form1 = ProfileForm(request.POST)
		form2 = WalletForm(request.POST) 
		if form1.is_valid() and form2.is_valid():
			profile = form1.save(commit=False)
			profile.user = request.user
			profile.save()

			wallet = form2.save(commit=False)
			wallet.balance = 100
			wallet.user = request.user
			wallet.save()
			return redirect(reverse('dashboard'))

	else:
		form1 = ProfileForm()
		form2 = WalletForm()

	return render(request, 'completeprofile.html', {'form1':form1, 'form2':form2})

def recharge(request):
	return render(request,'recharge.html')


def charge(request):
    if request.method == "POST":
        amount = int(request.POST['amount'])

        print('Data:', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.user.email,
            name=request.user.username,
            source=request.POST['stripeToken']
            )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='INR',
            description="Donation"
            )

        Wallet.objects.filter(balance=request.user.wallet.balance).update(balance=F('balance')+ amount)

        return redirect('recharge')
    return redirect('recharge')

def updateprofilepic(request):
	prof = request.user.profile
	form = ProfileForm(instance=prof)

	if request.method == "POST":
		form = ProfileForm(request.POST,request.FILES,instance=prof)
		if form.is_valid():
			
			form.save()
			return redirect(reverse('dashboard'))

	else:
		form = ProfileForm(instance=request.user.profile)

	return render(request, 'editprofilepic.html', {'form':form})

def updateprofile(request):
	if request.method == "POST":
		form = EditProfileForm(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			return redirect(reverse('dashboard'))

	else:
		form = EditProfileForm(instance=request.user)
		context = { 'form': form }

		return render(request, 'editprofile.html', context)

def updateastroprofile(request):
	if request.method == "POST":
		form = AstroProfileForm(request.POST,instance=request.user.profile.astro_profile)
		if form.is_valid():
			form.save()
			return redirect(reverse('dashboard'))

	else:
		form = AstroProfileForm(instance=request.user.profile.astro_profile)
		context = { 'form': form }

		return render(request, 'editastroprofile.html', context)