from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, ManyToManyField, OneToOneField
from django_mysql.models import ListTextField
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField

from job.models import Job


class User(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), null=True, blank=True, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    user_type = CharField(max_length=15, blank=True, null=True)
    avatar = ProcessedImageField(upload_to='uploaded/users/pro_img',

                                 format='JPEG',
                                 options={'quality': 60}, null=True, blank=True)


class WorkSchedule(models.Model):
    employee = models.ForeignKey('user.EmployeeProfile', null=True)

    how_time = CharField(max_length=15, blank=True, null=True)
    field_of_work = CharField(max_length=15, blank=True, null=True)
    abilities_have = ListTextField(
        base_field=models.CharField(max_length=20),
        size=6,
    )

    def __str__(self):
        return self.employee.user.username + ' ' + self.field_of_work


class EmployerProfile(models.Model):
    user = models.OneToOneField(User, null=True)

    company_name = CharField(max_length=15, blank=True, null=True)
    # Remember Many to Many fields doesn't show in mysql commend line
    job_offer = ManyToManyField(Job, blank=True)

    def __str__(self):
        return self.user.username


class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, null=True)
    # Remember Many to Many fields doesn't show in mysql commend line
    job_recommended = ManyToManyField(Job, blank=True)

    work_schedule = ManyToManyField(WorkSchedule, blank=True)

    def __str__(self):
        return self.user.username
