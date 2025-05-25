from datetime import timedelta
import calendar
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from core.models import Commit
from core import utils

import plotly.express as px

# Create your views here.

@login_required
def commits(request):
    now = timezone.now()
    start = now - timedelta(days=364)
    all_commits = Commit.objects.filter(user=request.user).order_by('created')
    daterange = utils.date_range(start, now)

    counts = [[] for i in range(7)]
    dates = [[] for i in range(7)]

    for dt in daterange:
        count = all_commits.filter(created__date=dt).count()
        day_number = dt.weekday()
        counts[day_number].append(count)
        dates[day_number].append(dt)

    day_names = list(calendar.day_name)

    first_day = daterange[0].weekday()
    days = day_names[first_day:] + day_names[:first_day]

    fig = px.imshow(
        counts,
        color_continuous_scale='greens',
        x=dates[0],
        y=days,
        height=320,
        width=1300,
    )
    fig.update_layout(plot_bgcolor='white')
    fig.update_traces({'xgap': 5, 'ygap': 5})

    chart = fig.to_html()

    context = {'chart': chart}
    return render(request, 'commits.html', context)