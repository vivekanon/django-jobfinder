from django.conf.urls import url

from user.api.views import UserCreateApiView, UserListApiView, UserDetailApiView, EmployerProfileCreateApiView, \
    EmployeeProfileCreateApiView, EmployeeProfileApiView, EmployerProfileApiView, ScheduleListApiView, \
    ScheduleCreateApiView, JobCreateApiView, JobListApiView

urlpatterns = [
    url(r'^$', UserListApiView.as_view(), name='UserListApi'),

    url(r'^employee/schedule/$', ScheduleListApiView.as_view(), name='ScheduleList'),
    url(r'^employee/schedule/create/$', ScheduleCreateApiView.as_view(), name='ScheduleCreateApi'),
    url(r'^employee/job/$', JobListApiView.as_view(), name='JobListApi'),

    url(r'^job/create/$', JobCreateApiView.as_view(), name='JobCreateApi'),

    url(r'^employer/create/$', EmployerProfileCreateApiView.as_view(), name='EmployerProfileCreateApi'),
    url(r'^employee/create/$', EmployeeProfileCreateApiView.as_view(), name='EmployeeProfileCreateApi'),

    url(r'^employer/detail/(?P<pk>\w+)$', EmployerProfileApiView.as_view(), name='EmployerProfileApi'),

    url(r'^employee/detail/(?P<pk>\w+)$', EmployeeProfileApiView.as_view(), name='EmployeeProfileApi'),

    url(r'^register/$', UserCreateApiView.as_view(), name='create-user'),
    url(r'^detail/(?P<pk>\w+)/$', UserDetailApiView.as_view(), name='user-detail'),

]
