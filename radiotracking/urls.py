"""Defines URL patterns for the 'radiotracking' app."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Show all programs
    url(r'^programs/$', views.programs, name='programs'),

    # Page for adding a new program
    url(r'^add_program/$', views.add_program, name='add_program'),

    # Detail page for a single program
    url(r'^programs/(?P<program_id>\d+)/$', views.program, name='program'),

    # Page for editing a program.
    url(r'^edit_program/(?P<program_id>\d+)/$', views.edit_program,
    name='edit_program'),

]
