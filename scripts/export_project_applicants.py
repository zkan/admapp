from django_bootstrap import bootstrap
bootstrap()

import sys
import json

from regis.models import Applicant
from appl.models import AdmissionProject, AdmissionRound, ProjectApplication

def load_tcas_data(filename):
    lines = open(filename).readlines()

    count = len(lines) // 2

    tcas_data = {}
    
    for i in range(count):
        nat_id = lines[i*2].strip()
        data = json.loads(lines[i*2+1].strip())

        if 'StatusMessage' in data:
            tcas_data[nat_id] = { 'status': 'missing' }
            continue

        tcas_data[nat_id] = {
            'status': 'found',
            'prefix': data['Prefix'],
            'first_name': data['Name'],
            'last_name': data['Surname']
        }
        
    return tcas_data

def main():
    project_id = sys.argv[1]
    round_id = sys.argv[2]

    tcas_data_filename = sys.argv[3]
    tcas_data = load_tcas_data(tcas_data_filename)

    project = AdmissionProject.objects.get(pk=project_id)
    admission_round = AdmissionRound.objects.get(pk=round_id)

    project_applications = ProjectApplication.find_for_project_and_round(project,
                                                                         admission_round,
                                                                         True)

    not_found_list = []
    
    for app in project_applications:
        if app.has_paid():
            try:
                majors =  app.major_selection.get_majors()
            except:
                majors = []
            applicant = app.applicant
            if applicant.has_registered_with_passport():
                nat = applicant.passport_number
            else:
                nat = applicant.national_id

            is_found = False
            if nat in tcas_data:
                if tcas_data[nat]['status'] == 'found':
                    is_found = True
                    
                    applicant.prefix = tcas_data[nat]['prefix']
                    applicant.first_name = tcas_data[nat]['first_name']
                    applicant.last_name = tcas_data[nat]['last_name']
                
                
            profile = applicant.get_personal_profile()
            app_date = '%02d/%02d/%04d' % (app.applied_at.day,
                                     app.applied_at.month,
                                     app.applied_at.year + 543)
            phone = profile.contact_phone
            if phone == '-':
                phone = profile.mobile_phone
            phone = phone.replace('-','')
            
            for m in majors:
                items = [
                    m.get_full_major_cupt_code(),
                    m.faculty.title,
                    m.title,
                    project.title,
                    app.get_number(),
                    nat,
                    applicant.prefix,
                    applicant.first_name,
                    applicant.last_name,
                    phone,
                    applicant.email,
                    app_date,
                ]
                out_line = ','.join(['"'+str(x)+'"' for x in items])
                if is_found:
                    print(out_line)
                else:
                    not_found_list.append(out_line)

    print()
    for l in not_found_list:
        print(l)
        

if __name__ == '__main__':
    main()
    