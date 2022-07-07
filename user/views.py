from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .user_forms import UserSignup
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'main.html')


def signup(request):
    if request.method == 'POST':
        request_form = UserCreationForm(request.POST or None)
        if request_form.is_valid():
            request_form.save()
            messages.success(request, 'Sign up Completed Successfully, Login from above')
    signup_form = UserSignup()
    return render(request, 'signup.html', {'signup_form': signup_form})
