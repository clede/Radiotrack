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

]
