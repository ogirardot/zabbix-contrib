from django.shortcuts import render
from django.db.models import Sum
from datetime import datetime

from frontend.models import Contribution


def index(request,
          template_name="index.html"):
    latest_contribs = Contribution.objects.order_by('-created_at')[:10]
    popular_contribs = Contribution.objects\
        .annotate(rating=Sum('votes'))\
        .filter(rating__gt=0)\
        .order_by('-rating')[:10]
    return render(request, template_name,
        {
            'latest_contribs': latest_contribs,
            'popular_contribs': popular_contribs,
        })


def about(request,
          template_name="about.html"):
    return render(request, template_name)
