from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from dashboard.models import HomePage, Register, Profile
from dashboard.forms import RegistrationForm, ProfileForm, HomePageForm

# Create your views here.

class HomePageView(ListView):
    model = HomePage
    template_name = 'dashboard/home.html'


class RegisterView(CreateView):
    model = Register
    template_name = 'dashboard/register.html'
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse('dashboard:Profile', kwargs={'pk' :self.object.pk})


class ProfileView(CreateView):
    model = Profile
    template_name = 'dashboard/profile.html'
    form_class = ProfileForm

    def post(self, request, pk):
        data = ProfileForm(request.POST, request.FILES)
        user = get_user_model().objects.filter(pk=pk).first()
        if data.is_valid():
            user_data = data.save(commit=False)
            user_data.owner = user
            user_data.save()
        return redirect(reverse('dashboard:HomePage'))

@login_required()
def ProfileInfoView(request):
    user = request.user
    user_data = get_user_model().objects.get(pk=user.pk)
    profile_data = Profile.objects.get(owner=user)
    return render(request, 'dashboard/profile-info.html', context={'user':user_data, 'profile_data':profile_data})


class CreatePostView(LoginRequiredMixin, CreateView):
    model = HomePage
    form_class = HomePageForm
    template_name = 'dashboard/post.html'

    def post(self, request):
        user = request.user
        data = HomePageForm(request.POST, request.FILES)
        if data.is_valid():
            user_data = data.save(commit=False)
            user_data.owner = user
            user_data.save()
        return redirect(reverse('dashboard:HomePage'))

