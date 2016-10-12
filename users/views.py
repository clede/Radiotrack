from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationFormTZ

def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('radiotracking:index'))

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationFormTZ()
    else:
        # Process completed form.
        form = UserCreationFormTZ(data=request.POST)

        if form.is_valid():
            new_user, userprofile = form.save()
            # Log the user in and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username,
                                 password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('radiotracking:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
