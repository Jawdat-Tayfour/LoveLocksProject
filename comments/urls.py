from django.urls import path


from .views import CommentView

urlpatterns = [
    
    path('padlocks/<int:pk>/comment/',CommentView.as_view(),name='create_comment'),

]
