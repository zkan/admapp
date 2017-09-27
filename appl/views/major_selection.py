# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseForbidden, HttpResponseServerError

from regis.models import Applicant
from appl.models import AdmissionProject, AdmissionRound, Major, MajorSelection, Faculty

from regis.decorators import appl_login_required

# def get_all_majors(request):
#     return 

def process_selection_form(request,
                           applicant,
                           application,
                           major_selection):
    if 'major' not in request.POST:
        return (True, 'คุณยังไม่ได้เลือกสาขา')
    number = request.POST['major']
    major = Major.get_by_project_number(application.admission_project,
                                        number)
    if not major:
        return (True, 'สาขาที่คุณเลือกผิดพลาด')

    major_selection.set_majors([major])
    major_selection.applicant = applicant
    major_selection.project_application = application
    major_selection.admission_project = application.admission_project
    major_selection.admission_round = application.admission_round
    major_selection.save()
    return (False, '')

@appl_login_required
def select(request, admission_round_id):
    applicant = request.applicant
    admission_round = get_object_or_404(AdmissionRound, pk=admission_round_id)

    if not admission_round.is_available:
        return HttpResponseForbidden()

    application = applicant.get_active_application(admission_round)
    if not application:
        return HttpResponseForbidden()

    project = application.admission_project
    
    try:
        major_selection = application.major_selection
    except MajorSelection.DoesNotExist:
        major_selection = MajorSelection(major_list='')

    if project.max_num_selections != 1:
        return HttpResponseServerError('Not implemented')

    error_message = ''

    major = None
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect(reverse('appl:index'))
        error, error_message = process_selection_form(request,
                                                      applicant,
                                                      application,                                             major_selection)
        if not error:
            return redirect(reverse('appl:index'))

    else:
        if major_selection.num_selected == 1:
            major = major_selection.get_majors()[0]

    majors = project.major_set.all()
    majors_dic = dict([(m.faculty_id, True) for m in majors])
    faculties = [f for f in Faculty.objects.all()
                  if f.id in majors_dic]

    return render(request,
                  'appl/major_multiple_selection.html',
                  { 'applicant': applicant,
                    'admission_project': project,
                    'admission_round': admission_round,
                    'application': application,
                    'major': major,
                    'faculties': faculties,
                    'all_majors': majors,
                    'error_message': error_message })
    
