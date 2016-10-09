from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Program, Station
from .forms import ProgramForm, StationForm

# Create your views here.
def index(request):
    """The home page for the 'radiotracking' app."""
    return render(request, 'radiotracking/index.html')

def check_program_owner(program):
    if program.owner != request.user:
        raise Http404

@login_required
def programs(request):
    """Show all programs."""
    programs = Program.objects.filter(owner=request.user).order_by('title')
    context = {'programs': programs}
    return render(request, 'radiotracking/programs.html', context)

@login_required
def add_program(request):
    """Add a new program."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ProgramForm()
    else:
        # POST data submitted; process data.
        form = ProgramForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            # Set the current user as owner of the newly-added program.
            new_program = form.save(commit=False)
            new_program.owner = request.user
            new_program.save()
            return HttpResponseRedirect(reverse('radiotracking:programs'))

    context = {'form': form}
    return render(request, 'radiotracking/add_program.html', context)

@login_required
def program(request, program_id):
    """Show a single program and all the info about it."""
    program = Program.objects.get(id=program_id)
    check_program_owner(program)
    context = {'program': program, }
    return render(request, 'radiotracking/program.html', context)

@login_required
def edit_program(request, program_id):
    """Edit an existing program."""
    program = Program.objects.get(id=program_id)
    check_program_owner(program)
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

# Stations!!!

def stations(request):
    """Show all radio stations."""
    stations = Station.objects.order_by('name')
    context = {'stations': stations}
    return render(request, 'radiotracking/stations.html', context)

@login_required
def add_station(request):
    """Add a new radio station."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = StationForm()
    else:
        # POST data submitted; process data.
        form = StationForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            form.save() # This must be so simple due to our use of ModelForm?
            return HttpResponseRedirect(reverse('radiotracking:stations'))

    context = {'form': form}
    return render(request, 'radiotracking/add_station.html', context)

def station(request, station_id):
    """Show a single station and all the info about it."""
    station = Station.objects.get(id=station_id)
    context = {'station': station, }
    return render(request, 'radiotracking/station.html', context)

@login_required
def edit_station(request, station_id):
    """Edit an existing radio station."""
    station = Station.objects.get(id=station_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current station.
        form = StationForm(instance=station)
    else:
        # POST data submitted; process data.
        form = StationForm(instance=station, data=request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('radiotracking:station',
            args=[station.id]))
    context = {'station': station, 'form': form}
    return render(request, 'radiotracking/edit_station.html', context)
