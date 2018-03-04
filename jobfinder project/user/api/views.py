from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import views
from rest_framework.generics import \
    (ListAPIView,
     RetrieveAPIView,
     UpdateAPIView,
     DestroyAPIView,
     RetrieveUpdateAPIView,
     CreateAPIView)
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser

from rest_framework.permissions import \
    (AllowAny,
     IsAdminUser,
     IsAuthenticated,
     IsAuthenticatedOrReadOnly)
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from job.models import Job
from user.api.serializer import UserListSerializer, CreateUserSerializer, UserDetailSerializer, \
    CreateEmployerProfileSerializer, CreateEmployeeProfileSerializer, EmployeeProfileSerializer, \
    EmployerProfileSerializer, ScheduleListSerializer, ScheduleCreateSerializer, JobCreateSerializer, JobListSerializer
from user.models import User, EmployeeProfile, EmployerProfile, WorkSchedule


class UserListApiView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()

    def get_queryset(self, *args, **kwargs):
        queryset_list = User.objects.all()
        query = self.request.GET.get("q")  # ?q=...
        if query:
            queryset_list = User.objects.filter(phone_number=query).distinct()

        return queryset_list


class ScheduleListApiView(ListAPIView):
    serializer_class = ScheduleListSerializer
    queryset = WorkSchedule.objects.all()


class ScheduleCreateApiView(CreateAPIView):
    serializer_class = ScheduleCreateSerializer
    queryset = WorkSchedule.objects.all()


class UserCreateApiView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class UserDetailApiView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class EmployerProfileCreateApiView(CreateAPIView):
    serializer_class = CreateEmployerProfileSerializer
    queryset = EmployerProfile.objects.all()


class EmployerProfileApiView(RetrieveUpdateAPIView):
    serializer_class = EmployerProfileSerializer
    queryset = EmployeeProfile.objects.all()
    permission_classes = [AllowAny]


class EmployeeProfileCreateApiView(CreateAPIView):
    serializer_class = CreateEmployeeProfileSerializer
    queryset = EmployeeProfile.objects.all()


class EmployeeProfileApiView(RetrieveUpdateAPIView):
    serializer_class = EmployeeProfileSerializer
    queryset = EmployeeProfile.objects.all()
    permission_classes = [AllowAny]


class JobListApiView(ListAPIView):
    serializer_class = JobListSerializer
    queryset = Job.objects.all()


class JobCreateApiView(CreateAPIView):
    serializer_class = JobCreateSerializer
    queryset = Job.objects.all()
