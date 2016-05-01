from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Ticket
import json
# Create your views here.


def index(request):
    ticket_list = Ticket.objects.order_by('-day')
    template = loader.get_template('demo/UI.html')
    context = {
        'item_list': ticket_list,
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    return HttpResponse(template.render(context, request))

def domestic(request):
    ticket_list = Ticket.objects.order_by('-price')[:5]
    template = loader.get_template('demo/index.html')
    context = {
        'item_list': ticket_list,
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    return HttpResponse(template.render(context, request))
# def get_ticket(request, query_json):
#
