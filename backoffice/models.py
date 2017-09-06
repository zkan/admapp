from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from appl.models import Campus, Faculty, AdmissionProject

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    faculty = models.ForeignKey(Faculty,
                                verbose_name='คณะที่สังกัด',
                                default=None,
                                null=True,
                                blank=True)
    is_admission_admin = models.BooleanField(verbose_name='ดูแลข้อมูลทุกคณะ',
                                             default=False)

    admission_projects = models.ManyToManyField(AdmissionProject)

    def __str__(self):
        if self.faculty:
            return self.user.get_full_name() + ' (' + self.faculty + ')'
        elif self.is_admission_admin:
            return self.user.get_full_name() + ' (ADMADMIN)'
        else:
            return self.user.get_full_name()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()