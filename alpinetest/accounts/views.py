
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from .form import RegistrationForm, UserForm, UserProfileForm
from .models import Account, UserProfile
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.utils.encoding import force_text



# Create your views here.

def register(request):

    if request.method=="POST":

        form = RegistrationForm(request.POST)
        
        if form.is_valid():
     
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
          
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()

            user_account = Account.objects.get(email=email)
            user_profile = UserProfile()
            user_profile.user = user_account
            user_profile.save()

            current_site = get_current_site(request)
            mail_subject = 'Got New User'
            message = render_to_string('accounts/send_email.html', {
                'user':user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = 'basantakharel@gmail.com'
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
     
            messages.success(request, 'Thanks for choosing us')
            return redirect('login')
    else:
        form = RegistrationForm()
    context={
        'form':form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
  
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now looged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Login')
            return redirect('login')

    return render(request, 'accounts/login.html')


@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, "You are sucessfully logout")
    return redirect('login')


@login_required(login_url = 'login')
def dashboard(request):
 
    userprofileExist = UserProfile.objects.filter(user_id=request.user.id).exists()
    if userprofileExist:
        userprofile = UserProfile.objects.get(user_id=request.user.id)
        imgurl = userprofile.profile_picture.url
    else:
        imgurl = "https://www.w3schools.com/howto/img_avatar.png"
    context={
            "imgurl":imgurl,
           
        }
    return render(request, 'accounts/dashboard.html', context)



@login_required(login_url='login')
def edit_profile(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance = request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance = userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile has been updated. ')
            return redirect('edit_profile')
    else:
        user_form = UserForm(instance = request.user)
        profile_form = UserProfileForm(instance =userprofile)
    
    context={
        'user_form':user_form,
        'profile_form': profile_form,
        'userprofile':userprofile,
    }
    return render(request, 'accounts/edit_profile.html', context)



@login_required(login_url='login')
def change_password(request):
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if confirm_password == new_password:
            user = Account.objects.get(username__exact = request.user.username)
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                messages.success(request, "Your Password is updated Successfully")
                return redirect('change_password')
            else:
                messages.error(request, "Please Provide correct Password")
                return redirect('change_password')
        else:
            messages.error(request,"Password Doesnot match")
            return redirect('change_password')

    return render(request, 'accounts/change_password.html')
