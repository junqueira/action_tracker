# -*- coding: utf-8 -*-

import imp
from datetime import datetime

def importPath( filepath ):
    """ Import file from a given path
    """
    return imp.load_source('module.name', filepath)

def get_client_ip(request):
    """ Get IP from visitor
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip

def getCurrentApplication(request):
    """ Get current application
    """
    currentApplication = "common"

    # Get full request URL
    currentURL = request.get_full_path()

    # Remove end slash
    if currentURL.endswith("/"):
        currentURL = currentURL[0:-1]

    # Split URL by /
    urlParts = currentURL.split("/")

    # Get first part of list
    if len(urlParts) > 1:
        currentApplication = urlParts[1]

    return currentApplication

