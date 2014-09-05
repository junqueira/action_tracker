# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import login as loginUser
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from users.forms import PasswordForm
#from apps.common import constants

@login_required
def Password(request):
    """ Password form
    """
    template_file = "user-password.html"
    form = PasswordForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        password = form.cleaned_data['password']
        new_password = form.cleaned_data['new_password']
        confirm_password = form.cleaned_data['confirm_password']

        if new_password != confirm_password:
            messages.add_message(request, messages.ERROR, u"The passwords don't match")
            return redirect("users:password")

        user = authenticate(username=request.user.username, password=password)

        if user is not None:
            if user.is_active:
                user.set_password(new_password)
                user.save()
            else:
                messages.add_message(request, messages.ERROR, u"The user is inactive")
                return redirect("home")
        else:
            messages.add_message(request, messages.ERROR, u"Invalid user or password")
            return redirect("users:password")

        messages.add_message(request, messages.SUCCESS, u"Password changed successfully")

        return redirect("home")

    params = {
        'form': form,
    }
    context = RequestContext(request)

    return render_to_response (
        template_file,
        params,
        context_instance = context
    )


