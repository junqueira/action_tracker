from django.shortcuts import render_to_response
from django.template import RequestContext

def Home(request):
    template_file = "home.html"
    context = RequestContext(request)
    params = {}

    return render_to_response (
        template_file,
        params,
        context_instance = context
    )


