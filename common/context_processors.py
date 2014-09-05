# -*- coding: utf-8 -*-

from common.utilities import getCurrentApplication

def global_vars(request):
    params = {
        'CURRENT_APPLICATION': getCurrentApplication(request),
    }

    return params

