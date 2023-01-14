from django.http import HttpResponseNotFound

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound


def passcard_info_view(request, passcode):
    visits = Visit.objects.filter(passcard__passcode=passcode).select_related('passcard')
    if not visits:
        raise Http404

    this_passcard_visits = []

    for visit in visits:
        total_seconds = visit.get_duration()
        is_strange = visit.is_visit_long(total_seconds)

        this_passcard_visits.append(
            {'entered_at': visit.entered_at,
             'duration': visit.format_duration(total_seconds),
             'is_strange': "Да" if is_strange else "Нет",
             },
        )
    context = {
        'passcard': passcode,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
