from django.http import HttpResponseRedirect
from django.conf import settings
from rickroll.exceptions import HackingAttempt


class HackingAttemptMiddleware(object):

    def get_redirect_url(self):
        try:
            url = settings.RICKROLL_URL
        except AttributeError:
            url = 'http://www.youtube.com/watch?v=dQw4w9WgXcQ'
        return url

    def process_exception(self, request, exception):
        if isinstance(exception, HackingAttempt):
            return HttpResponseRedirect(self.get_redirect_url())
