from django.shortcuts import redirect
from django.contrib import messages

def anonymous_required( view_function ):
    return AnonymousRequired( view_function )

class AnonymousRequired( object ):
    def __init__( self, view_function ):
        self.view_function = view_function

    def __call__( self, request, *args, **kwargs ):
        if request.user is not None and request.user.is_authenticated():
            return redirect("home")

        return self.view_function( request, *args, **kwargs )

