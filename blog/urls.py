from django.urls import path
from .views import (HomePageView,
                    BlogPageView, 
                    BlogDetailView, 
                    AboutPageView, 
                    PostCreateView, 
                    PostEditView,
                    DeletePostView)
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', BlogPageView.as_view(), name='post'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post_details/<int:pk>', BlogDetailView.as_view(), name='post_details'),
    path('/post/<int:pk>/edit', PostEditView.as_view(), name='post_edit'),
    path('/post/<int:pk>/delete', DeletePostView.as_view(), name='post_delete'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]