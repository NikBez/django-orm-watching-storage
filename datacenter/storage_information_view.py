from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

def storage_information_view(request):

    visits = Visit.objects.filter(leaved_at=None).select_related("passcard")
    non_closed_visits = []

    for visit in visits:
        total_seconds = visit.get_duration()
        format_duration = visit.format_duration(total_seconds)
        is_strange = visit.is_visit_long(total_seconds)

        non_closed_visits.append({'who_entered': visit.passcard.owner_name,
                                  'entered_at': visit.entered_at,
                                  'duration': format_duration,
                                  'is_strange': "Да" if is_strange else "Нет",
                                  })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
