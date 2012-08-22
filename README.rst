===============
Django Rickroll
===============
A novel way of handling malicious requests within a Django application.

Installation
------------
Install from PyPi (stable)::

    pip install django-rickroll

or Github (dev)::

    pip install -e git://github.com/codeinthehole/django-rickroll.git#egg=django-rickroll

Add ``'rickroll'`` to your ``INSTALLED_APPS`` and the following to your
``MIDDLEWARE_CLASSES``::

    'rickroll.middleware.HackingAttemptMiddleware'

Usage
-----
Wherever you detect a hacking attempt, raise a ``HackingAttempt`` exception
and the middleware will rickroll the offending user.  

For example, in your ``views.py``::

    from rickroll.exceptions import HackingAttempt

    def some_view(request):
        # ...
        if hacking_detected:
            raise HackingAttempt()

then the user in question will get redirected to http://www.youtube.com/watch?v=dQw4w9WgXcQ.
The destination can be overridden using the setting ``RICKROLL_URL``.

Discussion
----------
If your site ever gets penetration tested, the testing company will likely manipulate
every request to your site where there are parameters being passed (query
parameters, POST params, cookies etc).  When you encounter a parameter which
should be an integer but has value ``../../../../../../etc/passwd``, it's not
always clear what the "right" response should be. I thought it would be funny
to rickroll.
