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

def program(request, program_id):
    """Show a single program and all the info about it."""
    program = Program.objects.get(id=program_id)
    context = {'program': program, }
    return render(request, 'radiotracking/program.html', context)

def edit_program(request, program_id):
    """Edit an existing program."""
    program = Program.objects.get(id=program_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current program.
        form = ProgramForm(instance=program)
    else:
        # POST data submitted; process data.
        form = ProgramForm(instance=program, data=request.POST)
        if form.is_valid():
            form.save()

            # Not completely sure if this next bit should be programs or program
            return HttpResponseRedirect(reverse('radiotracking:program',
            args=[program.id]))
    context = {'program': program, 'form': form}
    return render(request, 'radiotracking/edit_program.html', context)
