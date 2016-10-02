from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Program
from .forms import ProgramForm

# Create your views here.
def index(request):
    """The home page for the 'radiotracking' app."""
    return render(request, 'radiotracking/index.html')

def programs(request):
    """Show all programs."""
    programs = Program.objects.order_by('title')
    context = {'programs': programs}
    return render(request, 'radiotracking/programs.html', context)

def add_program(request):
    """Add a new program."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ProgramForm()
    else:
        # POST data submitted; process data.
        form = ProgramForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            form.save() # This must be so simple due to our use of ModelForm?
            return HttpResponseRedirect(reverse('radiotracking:programs'))

    context = {'form': form}
    return render(request, 'radiotracking/add_program.html', context)
