from datetime import datetime


from django.shortcuts import render
from django.views.generic import UpdateView
from django.http  import HttpResponseRedirect
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy , reverse
from django.shortcuts import redirect



from locks.models import LockRequest
from .models import PadLock
from users.models import CustomUser
from .forms import PadLockForm



def create_padlock(request):
    user= request.user
    submitted = False 
    if request.method == "POST":
        form=PadLockForm(request.POST)
        if form.is_valid():
            user.lock_exist = True
            user2 =CustomUser.objects.get(username=user.user_locked_with)
            user2.lock_exist = True 
            model_instance = form.save(commit=False)
            model_instance.creator = user
            model_instance.modifier = user2 
            model_instance.save()
            user.save()
            user2.save()
            return HttpResponseRedirect("/?submitted=True")
    else:
        form = PadLockForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'create_padlock.html',{'form':form,'submitted':submitted})


class PadLockDetail(DetailView):
    model = PadLock
    template_name = 'padlock_detail.html'
    
def search_padlocks(request):
    if request.method == "POST":
        search_bar = request.POST['search_bar']
        if request.user.user_is_sender:
            padlocks_result = PadLock.objects.filter(motto_field__icontains=search_bar).exclude(creator=request.user)
        if request.user.user_is_reciever:
            padlocks_result = PadLock.objects.filter(motto_field__icontains=search_bar).exclude(modifier=request.user)
        return render(request,'search_padlocks.html',{'search_bar':search_bar,'padlocks_result':padlocks_result,})
    else:
        return render(request,'search_padlocks.html',{})
    
    
@login_required
def edit_padlock(request,pk):
    
    # dictionary for initial data with
    # field names as keys
    context ={}
    user = request.user 
    user2 = CustomUser.objects.get(username = user.user_locked_with)
    
    # fetch the object related to passed id
    obj = PadLock.objects.get(id=pk)
    
    # pass the object as instance in form
    form = PadLockForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        
        user.lock_published = True 
        user2.lock_published = True
        user.save()
        user2.save()
        form.save()
        try:
            padlock = PadLock.objects.get(modifier=request.user)
            padlock.active_state = True
            
            padlock.save()
        except:
            padlock = PadLock.objects.get(creator=request.user)
            padlock.active_state = True
            
            padlock.save()
        return HttpResponseRedirect('/')

    # add form dictionary to context
    try:
        padlock = PadLock.objects.get(modifier=request.user)
    except:
        padlock = PadLock.objects.get(creator=request.user)
    context['pk'] = padlock.id     
    context["form"] = form
    return render(request, "edit_padlock.html", context)

def home(request):
    if request.user.is_authenticated:    
        
        
        padlocks_posts = PadLock.objects.exclude(creator=request.user).exclude(modifier=request.user)

        
        # lr is List_of_requests but I was so dump to name in a better way, and now, too tired to rename it.

        allusers = CustomUser.objects.exclude(username=request.user)
        
        lr=LockRequest.objects.filter(user2=request.user)
        
        return render(request,'home.html',{'allusers':allusers,'lr':lr,'padlocks_posts':padlocks_posts})
    else:



        
        return render(request,'home.html')


