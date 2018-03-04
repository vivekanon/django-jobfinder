from django.db import models
from django.db.models import CharField, ForeignKey, OneToOneField
from django_mysql.models import ListTextField


class Job(models.Model):
    employer = ForeignKey('user.EmployerProfile', related_name='job', blank=True)
    field_of_work = CharField(max_length=15, blank=True, null=True)
    how_time = CharField(max_length=15, blank=True, null=True)
    abilities_needed = ListTextField(

        base_field=models.CharField(max_length=20),
        size=6,
    )


class JobOpportunity(models.Model):
    job = ForeignKey('job.Job', related_name='JobOpportunity', blank=True)
    employee = OneToOneField('user.EmployeeProfile')
