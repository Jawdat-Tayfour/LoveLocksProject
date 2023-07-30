from django.urls import path 


from .views import accept_request,decline_request

urlpatterns = [
     path('approve_lock/<int:id>/',accept_request,name='approve'),
     path('decline_lock/<int:id>/',decline_request,name='decline'),
     
]

