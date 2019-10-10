from os import name

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse
from .models import Questionnaire, Stock, Sector, Industry, UserProfile, StockRecommendation
from django.contrib.postgres.search import SearchVector
from .filters import Stockfilter
import django_filters
import pandas as pd
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import requests
import json


# Create your views here.

def recommend(request):
    if request.method == 'POST':
        data = request.POST
        sector = Sector.objects.get(name=data['sector'])
        industry = Industry.objects.get(name=data.get('industry'))
        questionnaire = Questionnaire.objects.create(
            gender=data['gender'],
            risk=data.get('risk'),
            csr=data.get('csr'),
            hr=data.get('hr'),
            Female_exec=data.get('Female_exec')
        )
        questionnaire.sector.add(sector)
        questionnaire.industry.add(industry)
        questionnaire.save()
        return redirect('get_stock', questionnaire=questionnaire.pk)

    return render(request, 'recommendation/template_view.html')


def get_stock(request, questionnaire):
    questionnaire = get_object_or_404(Questionnaire, pk=questionnaire)
    print(questionnaire)
    stock_filter = Stock.objects.filter(
        Q(sector__in=questionnaire.sector.all()) | Q(industry__in=questionnaire.industry.all()))

    for stock in stock_filter:
        print(type(stock), stock)
    return render(request, 'recommendation/stock.html', {'filter': stock_filter, 'questionnaire': questionnaire})


def stock_filter(args):
    pass


def create_profile(request, questionnaire):
    if request.method == 'POST':
        print(request.POST)
        questionnaire=get_object_or_404(Questionnaire, pk=questionnaire)
        print(questionnaire)

        '''manually checks if this username already exists in database'''
        if User.objects.filter(username=request.POST['username']).exists():
            return HttpResponse('Username taken', status=400)

        '''Grabs information from form signup.html to create a user'''
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email']
        )
        user.save()
        user = authenticate(username=user.username, password=request.POST['password'])
        if user:
            login(request, user)

        print('in here')

        myprofile = UserProfile(
            user=user,
            questionnaire=questionnaire,
            user_gender=questionnaire.gender,
            user_email=user.email
        )
        myprofile.save()

        stock_filter = Stock.objects.filter(
                Q(sector__in=questionnaire.sector.all()) | Q(industry__in=questionnaire.industry.all()))
        for stock in stock_filter:
            rec = StockRecommendation(stock=stock, user=myprofile)
            rec.save()

        return redirect(reverse('profile'))

    else:

        form = UserCreationForm()
    return render(request, 'recommendation/signup.html', {'form': form, 'questionnaire': questionnaire})


def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    stock_filter=StockRecommendation.objects.filter(user=profile)
    # rec = StockRecommendation.objects.get(stock=stock_filter(),user=profile.user)

    #Grab Stock News
    api_request = requests.get(
        "https://stocknewsapi.com/api/v1/category?section=general&items=50&token"
        "=w3i80kjldorq6llswx65o3slp2altw4nsr3qhd1j")

    api = json.loads(api_request.content)

    print(profile, profile.user)

    return render(request, 'recommendation/profile.html', {'filter': stock_filter, 'profile': profile, 'api': api})


def login_user(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('profile')
        else:
            messages.success(request, 'Error logging in - please sign up..')
            return redirect('signup')
    else:
        return render(request, 'recommendation/profile.html')