#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render_to_response, render, redirect
from .models import Ticket
from .forms import Search

# Create your views here.


def index(request):
    if request.method == 'GET':
        search_form = Search(request.GET)

    ticket_list = Ticket.objects.order_by('-day')
    template = loader.get_template('demo/UI.html')
    context = {
        'item_list': ticket_list,
    }

    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    return HttpResponse(template.render(context, request))

def domestic(request):
    ticket_list = Ticket.objects.order_by('price')[:5]
    template = loader.get_template('demo/index.html')
    context = {
        'item_list': ticket_list,
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    return HttpResponse(template.render(context, request))
# def get_ticket(request, query_json):
