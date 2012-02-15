from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render
from jinja2 import Markup

from flicks.base.util import absolutify, redirect
from flicks.videos.vidly import embedCode


def home(request):
    """Landing page for Flicks. Displays only the promo videos."""
    # Redirect logged in users to the recent videos page.
    if request.user.is_active:
        return redirect('flicks.videos.recent')

    d = dict(promo_dance=settings.VIDEO_PROMOS_DANCE,
             promo_noir=settings.VIDEO_PROMOS_NOIR,
             promo_twilight=settings.VIDEO_PROMOS_TWILIGHT,
             page_type='home')

    return render(request, 'home.html', d)


def creative(request):
    """Creative Brief page."""
    d = dict(
        promo_dance=absolutify(reverse('flicks.videos.promo_video_dance')),
        promo_noir=absolutify(reverse('flicks.videos.promo_video_noir')),
        promo_twilight=absolutify(
            reverse('flicks.videos.promo_video_twilight')),
        page_type='secondary'
    )

    return render(request, 'creative.html', d)


def judges(request):
    """Judges page."""
    return render(request, 'judges.html', {'page_type': 'secondary'})


def prizes(request):
    """Prizes page."""
    return render(request, 'prizes.html', {'page_type': 'secondary'})


def partners(request):
    """Partners page."""
    return render(request, 'partners.html', {'page_type': 'secondary'})


def faq(request):
    """FAQ page."""
    return render(request, 'faq.html')


def rules(request):
    """Contest Rules page."""
    return render(request, 'rules.html')
