from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseForbidden

from regis.models import Applicant
from appl.models import AdmissionProject, AdmissionRound
from appl.models import ProjectApplication, Payment

from backoffice.views.permissions import can_user_view_project
from backoffice.decorators import user_login_required

def load_applicant_round_paid_amount(admission_round):
    round_payments = Payment.objects.select_related('applicant').filter(admission_round=admission_round)

    paid_amount = {}
    for p in round_payments:
        if p.applicant:
            if p.applicant.national_id not in paid_amount:
                paid_amount[p.applicant.national_id] = 0
            paid_amount[p.applicant.national_id] += p.amount

    return paid_amount
        

@user_login_required
def index(request, project_id, round_id):
    user = request.user
    
    project = get_object_or_404(AdmissionProject, pk=project_id)
    admission_round = get_object_or_404(AdmissionRound, pk=round_id)
    if not can_user_view_project(user, project):
        return redirect(reverse('backoffice:index'))

    applicant_paid_amount = load_applicant_round_paid_amount(admission_round)
    
    project_applications = ProjectApplication.find_for_project_and_round(project,
                                                                         admission_round,
                                                                         True)
    major_map = dict([(m.number,m) for m in project.major_set.all()])
    applicants = []

    for app in project_applications:
        applicant = app.applicant

        try:
            major_selection = app.major_selection
            applicant.major_selection = major_selection
            applicant.majors = []
            for num in major_selection.get_major_numbers():
                applicant.majors.append(major_map[num])
            if project.max_num_selections == 1:
                if len(applicant.majors)!=0:
                    applicant.major_number = applicant.majors[0].number
                else:
                    applicant.major_number = 1000000000
        except:
            applicant.major_selection = None
            applicant.majors = []
            applicant.major_number = 1000000000

        admission_fee = app.admission_fee(project_base_fee=project.base_fee,
                                          majors=applicant.majors)
        applicant.has_paid = applicant_paid_amount.get(applicant.national_id,0) >= admission_fee
            
        applicants.append(applicant)

    if project.max_num_selections==1:
        amap = dict([(a.id,a) for a in applicants])
        sorted_applicants = [x[1] for x in sorted([(applicant.major_number,
                                                    applicant.id) for applicant
                                                   in applicants])]
        applicants = [amap[i] for i in sorted_applicants]

        sorted_by_majors = True
    else:
        sorted_by_majors = False
        
    return render(request,
                  'backoffice/show_project_in_round.html',
                  { 'project': project,
                    'admission_round': admission_round,
                    'applicants': applicants,
                    'sorted_by_majors': sorted_by_majors,
                  })
