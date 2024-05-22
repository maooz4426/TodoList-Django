from django.urls import path
from .views import SignupView,CustomLoginView,CustomLogoutView

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignupView.as_view(),name='sighup'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',CustomLogoutView.as_view(),name='logout'),
]