from django_bootstrap import bootstrap
bootstrap()

import sys
import csv

from django.contrib.auth.models import User
from appl.models import AdmissionProject, Faculty

def main():
    filename = sys.argv[1]
    counter = 0
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        first = True
        for items in reader:
            if first:
                first = False
                continue

            if len(items) < 6:
                continue
            username = items[0]
            email = username + '@fake.admission.ku.ac.th'
            password = items[3]

            old_user = User.objects.filter(username=username)
            if len(old_user) >= 1:
                user = old_user[0]
                user.email = email
                user.set_password(password)
            else:
                user = User.objects.create_user(username, email, password)

            user.first_name = items[1].strip()
            user.last_name = items[2].strip()
            user.save()

            project = AdmissionProject.objects.get(pk=items[4])
            faculty = Faculty.objects.get(pk=items[5])

            profile = user.profile
            profile.is_admission_admin = False
            profile.admission_projects.add(project)
            profile.faculty = faculty

            if len(items) >= 7:
                profile.major_number = int(items[6])
            
            profile.save()

            print(username)

            counter += 1

    print('Imported',counter,'users')
        

if __name__ == '__main__':
    main()
    
