from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model,login 
from django.contrib import messages
from django.core.mail import EmailMessage 
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy 
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str



from .tokens import account_activation_token
from .forms import CustomUserCreationForm
from .models import CustomUser
from locks.models import LockRequest




def send_request(request,id):
    from_user = request.user
    to_user= CustomUser.objects.get(id=id)
    if from_user.lock_count >0:
        lock_request = LockRequest.objects.get_or_create(user1=from_user,user2=to_user)
        return redirect('search_users')
    else:
        return redirect('search_users')


def search_users(request):
    if request.method == "POST":
        search_bar = request.POST['search_bar']
        users_result = CustomUser.objects.filter(username__icontains=search_bar).exclude(username=request.user.username)
        return render(request,'search_users.html',{'search_bar':search_bar,'user_result':users_result,})
    else:
        return render(request,'search_users.html',{})


def activate(request,uidb64,token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user =User.objects.get(pk=uid)
    except:
        user = None

    if user and account_activation_token.check_token(user, token):
        user.is_active = True 
        user.save()
        messages.success(request, "Account activated, thank you for confirming.")
        return redirect('home')
    else:
        messages.error(request,"Activation failed, link may be expired!")
        return redirect('home')


def activate_email(request,user,to_email):
    mail_subject = "Activate you account"
    message = render_to_string("activate_account_template.html",
                               {'user':user.username,
                                'domain':get_current_site(request).domain,
                                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                                'token':account_activation_token.make_token(user),
                                'protocol':'https' if request.is_secure() else 'http'}


    )
    email = EmailMessage(mail_subject,message,to=[to_email])
    if email.send():

        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request,f'There was a problem sending an email to {to_email}, check for typos.')


def sign_up_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False 
            user.save()
            activate_email(request,user,form.cleaned_data.get('email'))

            return redirect('login')
        else:
            for erorr in list(form.errors.values()):
                print(request,erorr)
    else:
        form = CustomUserCreationForm()
    return render(request,template_name='signup.html',context={'form':form})



