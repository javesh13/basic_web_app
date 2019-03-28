from .views import login, signup
from django.urls import path
urlpatterns = [
    path('login/', login.as_view(), name="login"),
    path('signup/', signup.as_view(), name="signup"),
]
