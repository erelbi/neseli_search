# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from django.conf.urls import url
from django.urls import path, re_path
from app import views
from app.searcbox import search


urlpatterns = [

    re_path(r'^.*\.html', views.pages, name='pages'),
    #  path('', views.index, name='home'),
    path('', search.Search.as_view(), name='home'),


]
