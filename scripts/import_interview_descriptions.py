from django_bootstrap import bootstrap
bootstrap()

import sys
import csv
import io

from appl.models import Campus, Faculty, AdmissionProject, AdmissionRound, Major, MajorInterviewDescription

def main():
    project_id = sys.argv[2]
    project = AdmissionProject.objects.get(pk=project_id)

    round_id = sys.argv[3]
    admission_round = AdmissionRound.objects.get(pk=round_id)

    filename = sys.argv[1]
    counter = 0
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for items in reader:
            if len(items) < 8:
                continue
            
            major_number = int(items[0])
            major = Major.objects.filter(admission_project=project, number=major_number)[0]

            desc = MajorInterviewDescription(major=major,
                                             admission_round=admission_round)
            desc.descriptions = items[7]
            desc.save()

            counter += 1
        
    print('Imported',counter,'majors')
        

if __name__ == '__main__':
    main()
    
