from datetime import datetime 


from django.shortcuts import render
from django.views.generic import  UpdateView
from django.urls import reverse


from users.models import CustomUser
from padlocks.models import PadLock
from comments.models import Comment


def profile_detail_view(request,pk):
    profile_user = CustomUser.objects.get(id=request.user.id)
    profile_padlock = None
    if profile_user.lock_published:
        try:
            profile_padlock= PadLock.objects.get(creator = profile_user)
        except Exception:
            profile_padlock= PadLock.objects.get(modifier = profile_user) #XX/YY/2023
        show_date = datetime.today()
        if show_date.month>=profile_padlock.start_date.month and show_date.day>=profile_padlock.start_date.day:
            show_date = datetime(day=show_date.day,month=show_date.month,year=profile_padlock.start_date.year-1)
    else:
        show_date = datetime.today()
    comment_list = Comment.objects.filter(creator=profile_user)
    
    return render(request,'profile_detail.html',{'object':profile_user,'profile_padlock':profile_padlock,'show_date':show_date,'comment_list':comment_list})
    

class ProfileUpdateView(UpdateView):
    model = CustomUser
    template_name = 'profile_update.html'
    fields = ('first_name','last_name',)
    def get_success_url(self):
            return reverse('profile_detail', kwargs={'pk': self.kwargs['pk']})
