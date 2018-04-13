from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import signupForm

# Create your views here.
def account(request):
	return render(request, 'accounts/signup.html')

def signup_view(request):
	if request.method == 'POST':
		form = signupForm(request.POST)
		if form.is_valid():
			return render(request, 'accounts/signup.html')