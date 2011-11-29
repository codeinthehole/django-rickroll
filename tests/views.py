from django.http import HttpResponse
from rickroll.exceptions import HackingAttempt


def normal_view(request):
    return HttpResponse()


def hacking_attempt(request):
    raise HackingAttempt("Naughty!")
