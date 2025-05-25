from datetime import timedelta

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from core.models import Commit
from core import utils

# Create your views here.

@login_required
def commits(request):
    now = timezone.now()
    start = now - timedelta(days=364)
    all_commits = Commit.objects.filter(user=request.user).order_by('created')
    daterange = utils.date_range(start, now)

    counts = []
    for dt in daterange:
        count = commits.filter(created__date=dt).count()
        counts.append(count)

    context = {}
    return render(request, 'commits.html', context)