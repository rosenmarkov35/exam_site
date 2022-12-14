from django import forms, views
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, TemplateView

from exam_site.auth_app.models import Profile


# REGISTRATION ONLY

class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location']

        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Not required.'}),
        }


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs[
            'placeholder'] = 'Think of a strong password! | at least 8 characters with letters.'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter the password above.'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        field_classes = {'username': UsernameField}

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }


class CreateUserProfileView(views.View):
    @staticmethod
    def post(request, *args, **kwargs):
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileCreationForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)

            profile.user = user
            messages.success(request, 'Your profile was successfully created!')
            return redirect('index')

        else:
            messages.error(request, 'Please correct the error below.')

    @staticmethod
    def get(request, *args, **kwargs):
        user_form = CustomUserCreationForm()
        profile_form = ProfileCreationForm()
        return render(request, 'auth/register.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })

    # class CreateProfileView(CreateView):
    #     template_name = 'auth/register.html'
    #     form_class = CustomUserCreationForm
    #     success_url = reverse_lazy('index')
    #     extra_context = {


# REGISTRATION ONLY


# LOGIN ONLY

class CustomAuthForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class': 'form-control'}),
    )


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    authentication_form = CustomAuthForm


# LOGIN ONLY


# LOGOUT ONLY

class MyLogoutView(LogoutView):
    next_page = reverse_lazy('index')


# LOGOUT ONLY


# PROFILE DETAILS ONLY

class ProfileDetailsView(LoginRequiredMixin, TemplateView):
    template_name = 'auth/profile_details.html'


# class BookDetailView(View):
#     def get(self, request, *args, **kwargs):
#         book = get_object_or_404(Book, pk=kwargs['pk'])
#         context = {'book': book}
#         return render(request, 'books/book_detail.html', context)
# PROFILE DETAILS ONLY

class ShoppingCartView(TemplateView):
    template_name = 'shopping_cart.html'
    extra_context = {}

