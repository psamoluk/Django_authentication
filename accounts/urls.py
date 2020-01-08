from django.urls import path
import accounts.views

urlpatterns = [
    path('', accounts.views.home, name='accounts'),
    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout')
]

