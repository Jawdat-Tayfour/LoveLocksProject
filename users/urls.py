from django.urls import path


from .views import sign_up_view,search_users,send_request,activate


urlpatterns = [
    path('create_lock/<int:id>/',send_request,name='create_lock'),
    path('serch_users',search_users, name= 'search_users'),
    path('signup/', sign_up_view, name='signup'),
    path('activate/<uidb64>/<token>',activate,name="activate"),
]
