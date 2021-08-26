#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 13:47:51 2021

@author: alina

Defines URL patterns for breathing_room_app.
"""

from django.urls import path
from . import views

app_name = "breathing_room_app"

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Exercises page
    path('exercises/', views.exercises, name='exercises'),
    # Board page
    # path('board/', views.board, name='board'),
    ]