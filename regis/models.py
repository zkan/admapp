from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password as check_hashed_password

from datetime import datetime

class Applicant(models.Model):
    national_id = models.CharField(max_length=16,
                                   unique=True)
    passport_number = models.CharField(max_length=20, blank=True)
    prefix = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    
    email = models.EmailField()

    hashed_password = models.CharField(max_length=128,
                                       blank=True)
    
    def __str__(self):
        return "%s%s %s (%s)" % (self.prefix,
                                 self.first_name,
                                 self.last_name,
                                 self.national_id)

    @staticmethod
    def find_by_national_id(national_id):
        try:
            applicant = Applicant.objects.get(national_id=national_id)
            return applicant
        except Applicant.DoesNotExist:
            return None

    def get_full_name(self):
        return "{0}{1} {2}".format(self.prefix, self.first_name, self.last_name)
        
    def set_password(self, password):
        self.hashed_password = make_password(password)
        
    def check_password(self, password):
        return check_hashed_password(password, self.hashed_password)

    def get_active_application(self, admission_round):
        applications = self.project_applications.filter(is_canceled=False, admission_round=admission_round).all()
        if len(applications) > 0:
            return applications[0]
        else:
            return None

    def apply_to_project(self, admission_project, admission_round):
        from appl.models import ProjectApplication

        application = ProjectApplication(applicant=self,
                                         admission_project=admission_project,
                                         admission_round=admission_round)
        application.applied_at = datetime.now()
        application.save()
        
        return application
        
