# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User

def Delete(request,user_id):
    obj = User.objects.get(pk=user_id)
    obj.delete()
    msg = u"User successfully deleted"
    messages.add_message(request, messages.SUCCESS, msg)
    return redirect("users:home")
