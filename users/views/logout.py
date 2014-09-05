# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import logout as logoutUser
from django.contrib.auth.decorators import login_required

@login_required
def Logout(request):
    """ Logout action
    """
    logoutUser(request)
    messages.add_message(request, messages.SUCCESS, u"You're now logged out")
    return redirect("home")
