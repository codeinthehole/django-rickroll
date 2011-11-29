===============
Django Rickroll
===============
A novel way of handling suspicious requests within a Django application.

Installation
------------
Install from PyPi::

    pip install django-rickroll

Add to ``rickroll`` to your ``INSTALLED_APPS`` and add the following to your
middleware::

    'rickroll.middleware.HackingAttemptMiddleware'

Usage
-----
Now, wherever you detect a hacking attempt, raise a ``HackingAttempt`` exception
and the middleware will rickroll the offending user.  For example, in your ``views.py``::

    from rickroll.exceptions import HackingAttempt

    def some_view(request):
       if hacking_detected:
           raise HackingAttempt()

then the user in question will get redirected to http://www.youtube.com/watch?v=oHg5SJYRHA0.
The destination can be overridden using the setting ``RICKROLL_URL``.

Enjoy.