from django.urls import path 


from .views import profile_detail_view, ProfileUpdateView

urlpatterns = [
    path('<int:pk>/',profile_detail_view,name='profile_detail'),
    path('edit_profile/<int:pk>',ProfileUpdateView.as_view(),name= 'profile_edit'),
]
