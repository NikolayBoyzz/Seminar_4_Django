from django.shortcuts import render
from django.http import HttpResponse

import logging

logger = logging.getLogger(__name__)


def index(request, *args, **kwargs):
    response = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Мой первый Django-сайт</title>
</head>
<body>

def index(request):
    return HttpResponse("Hello, world!")

def about(request):
    return HttpResponse("About us")

