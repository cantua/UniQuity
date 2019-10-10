from django.contrib.auth.forms import UserCreationForm
from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='recommendation/home.html'), name="home"),
    path('quiz', views.recommend, name="recommend"),
    path('login', views.login_user, name="login_user"),
    path('stocks/<int:questionnaire>', views.get_stock, name="get_stock"),
    path('signup/<int:questionnaire>', views.create_profile, name="signup"),
    path('profile/', views.profile, name="profile"),
]