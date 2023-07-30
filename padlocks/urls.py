from django.urls import path
from .views import home , create_padlock ,edit_padlock , PadLockDetail,search_padlocks
urlpatterns = [
    path('',home,name='home'),
    path("create_padlock/",create_padlock,name="create_padlock"),
    path('edit_padlock/<int:pk>/', edit_padlock, name='edit_padlock'),
    path('<int:pk>/',PadLockDetail.as_view(),name='padlock_detail'),
    path('search_padlocks/',search_padlocks, name= 'search_padlocks'),
]
