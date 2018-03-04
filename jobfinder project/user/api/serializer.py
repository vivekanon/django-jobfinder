import random
import re
import string

from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.forms import PasswordInput, forms
from django.http import JsonResponse
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer
, HyperlinkedIdentityField,
    SerializerMethodField,
    CharField

)
from django import forms
from rest_framework_jwt.compat import PasswordField
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler, JSONWebTokenSerializer

from job.models import Job, JobOpportunity
from user.models import EmployerProfile, User, EmployeeProfile, WorkSchedule
from user.proccess import check_abilities, check_abilities_for_employee


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'user_type']

    def create(self, validated_data):
        # test normalize too
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user_type = validated_data['user_type']

        phone_number = validated_data['phone_number']
        password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))

        user = User.objects.create(
            username=first_name + '' + last_name,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,

        )
        user.set_password(password)
        user.save()
        if user_type == 'employee':
            EmployeeProfile.objects.create(user=user)

        return validated_data

    def validate(self, data):
        print(1)

        try:
            if User.objects.get(phone_number=data['phone_number']):
                print(2)
                raise serializers.ValidationError("این شماره قبلا استفاده شده")

            return data

        except ObjectDoesNotExist:
            if len(data['phone_number']) > 11:
                raise serializers.ValidationError("شماره تلفن همراهتون نباید بیشتر از ۱۱ رقم باشه")

            return data


class ScheduleListSerializer(ModelSerializer):
    class Meta:
        model = WorkSchedule
        fields = ['user', 'field_of_work', 'how_time', 'abilities_have', ]


class ScheduleCreateSerializer(ModelSerializer):
    abilities_have = serializers.ListField(
        child=serializers.CharField()
    )

    class Meta:
        model = WorkSchedule
        fields = ['employee', 'field_of_work', 'how_time', 'abilities_have']

    def create(self, validated_data):
        # test normalize too
        employee = validated_data['employee']

        field_of_work = validated_data['field_of_work']
        abilities_have = validated_data['abilities_have']
        schedule = WorkSchedule.objects.create(
            employee=employee,
            field_of_work=field_of_work,

        )
        for item in abilities_have:
            schedule.abilities_have.append(item)
            schedule.save()

        employer = check_abilities_for_employee(abilities_have, field_of_work)
        job = Job.objects.get(employer=employer)
        JobOpportunity.objects.create(employee=employee, job=job)

        return validated_data


class UserListSerializer(ModelSerializer):
    username = SerializerMethodField()
    url = HyperlinkedIdentityField(
        view_name='api-users:user-detail',

    )

    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'user_type', 'url']

    def get_username(self, obj):
        return obj.first_name + ' ' + obj.last_name


class UserDetailSerializer(ModelSerializer):
    username = SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'user_type', 'avatar', ]

    def get_username(self, obj):
        return obj.first_name + ' ' + obj.last_name


class EmployerProfileSerializer(ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = EmployerProfile
        fields = ['user', 'company_name', 'job_offer']

    def get_user(self, obj):
        return UserDetailSerializer(obj.user, many=True).data


class EmployeeProfileSerializer(ModelSerializer):
    abilities_have = serializers.ListField(
        child=serializers.CharField()
    )

    class Meta:
        model = EmployeeProfile
        fields = ['job_recommended', ]

    def update(self, instance, validated_data):
        job = validated_data['job_recommended']
        instance.job_recommended.append(job)
        instance.save()
        return instance


class CreateEmployerProfileSerializer(ModelSerializer):
    abilities_have = serializers.ListField(
        child=serializers.CharField()
    )

    class Meta:
        model = EmployerProfile
        fields = ['user', 'company_name', 'job_offer', ]

    def create(self, validated_data):
        # test normalize too

        company_name = validated_data['company_name']
        job_offer = validated_data['job_offer']
        user = validated_data['user']

        EmployerProfile.objects.create(
            user=user,
            company_name=company_name,

        )

        return validated_data


class CreateEmployeeProfileSerializer(ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = ['user', 'job_recommended', ]

    def create(self, validated_data):
        # test normalize too
        user = validated_data['user']

        job_recommended = validated_data['job_recommended']
        employee_profile = EmployeeProfile.objects.create(
            user=user,

        )

        employee_profile.save()
        return validated_data


class JobListSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = ['user', 'field_of_work', 'how_time', 'abilities_needed', ]


class JobCreateSerializer(ModelSerializer):
    abilities_needed = serializers.ListField(
        child=serializers.CharField()
    )

    class Meta:
        model = Job
        fields = ['user', 'field_of_work', 'how_time', 'abilities_needed']

    def create(self, validated_data):
        # test normalize too
        user = validated_data['user']

        field_of_work = validated_data['field_of_work']
        abilities_needed = validated_data['abilities_needed']
        job = Job.objects.create(
            user=user,
            field_of_work=field_of_work,

        )
        for item in abilities_needed:
            job.abilities_needed.append(item)
            job.save()

        # ------ Lets Create Opportunity ------
        employee = check_abilities(abilities_needed, field_of_work)
        JobOpportunity.objects.create(employee=employee, job=job)
        return validated_data


class CustomJWTSerializer(JSONWebTokenSerializer):
    username_field = 'phone_number'

    def __init__(self, *args, **kwargs):
        """
        Dynamically add the USERNAME_FIELD to self.fields.
        """
        super(JSONWebTokenSerializer, self).__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField(write_only=True, required=False)

    def validate(self, attrs):
        print('1')
        user_obj = User.objects.filter(phone_number=attrs.get("phone_number")).first()
        print(user_obj)
        if user_obj is not None:
            print('1')
            payload = jwt_payload_handler(user_obj)
            return {
                'token': jwt_encode_handler(payload),

            }

        else:
            response_text = {"non_field_errors": ["این شماره در سیستم وجود نداره"]}
            return JsonResponse(response_text, status=status.HTTP_400_BAD_REQUEST)


class JobOpportunityListSerializer(ModelSerializer):
    class Meta:
        model = JobOpportunity
        fields = ['job', 'user']


class JobOpportunityCreateSerializer(ModelSerializer):
    abilities_needed = serializers.ListField(
        child=serializers.CharField()
    )

    class Meta:
        model = JobOpportunity
        fields = ['job', 'employee']

    def create(self, validated_data):
        # test normalize too
        user = validated_data['user']

        field_of_work = validated_data['field_of_work']
        abilities_needed = validated_data['abilities_needed']
        job = Job.objects.create(
            user=user,
            field_of_work=field_of_work,

        )
        for item in abilities_needed:
            job.abilities_needed.append(item)
            job.save()
        return validated_data
