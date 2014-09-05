# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from users.forms import UserForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User

def Edit(request,user_id):
    template_file = "user-edit.html"
    context = RequestContext(request)

    obj = User.objects.get(pk=user_id)

    form = UserForm(request.POST or None, request.FILES or None,instance=obj)
    if form.is_valid():
        mymodel = form.save()

        msg = u"User saved successfully"
        messages.add_message(request, messages.SUCCESS, msg)
        return redirect("users:home")

    params = {
        'form': form,
        'user_id': user_id,
    }

    return render_to_response (
        template_file,
        params,
        context_instance = context
    )
