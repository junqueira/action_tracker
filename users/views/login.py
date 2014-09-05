# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import login as loginUser
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from users.forms import LoginForm
from common.decorators import anonymous_required
from django.conf import settings

@anonymous_required
def Login(request):
    """ Login form
    """
    template_file = "user-login.html"
    form = LoginForm(request.POST or None, request.FILES or None)
    next = request.POST.get('next', None)

    if form.is_valid():
        username = form.cleaned_data['login']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                loginUser(request, user)
            else:
                messages.add_message(request, messages.ERROR, u"Inactive user")
                return redirect("users:login")
        else:
            messages.add_message(request, messages.ERROR, u"Invalid user or password")
            return redirect("users:login")


        msg = u"You're now logged in"
        messages.add_message(request, messages.SUCCESS, msg)

        if next is not None:
            return HttpResponseRedirect(next)

        return redirect("home")

    params = {
        'form': form,
    }

    if next is not None:
        params["next"] = next

    context = RequestContext(request)
    return render_to_response (
        template_file,
        params,
        context_instance = context
    )
