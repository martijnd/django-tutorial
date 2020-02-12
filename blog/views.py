# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

posts = [
    {
        'author': 'Martijn Dorsman',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    },
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
