# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
  response = "Hello this is a request"
  return HttpResponse(response)

def new(request):
  response = "This is a new item"
  return HttpResponse(response)

def create(request):
  response = "This is a redirect"
  return redirect('/')

def show(request):
  response = "This is a certain blog post"
  return HttpResponse(response)

def edit(request):
  response = "This is an edit route"
  return HttpResponse(response)

def destroy(request):
  response = "This is a destroy route"
  return HttpResponse(response)

# Create your views here.
