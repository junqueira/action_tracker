# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from users.forms import UserForm
from django.shortcuts import redirect
from django.contrib import messages

def New(request):
    template_file = "user-new.html"
    context = RequestContext(request)

    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        mymodel = form.save()

        msg = u"User successfully created"
        messages.add_message(request, messages.SUCCESS, msg)
        return redirect("users:home")

    params = {
        'form': form,
    }

    return render_to_response (
        template_file,
        params,
        context_instance = context
    )


