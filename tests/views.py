from rickroll.exceptions import HackingAttempt


def index(request):
    raise HackingAttempt("Naughty!")

