from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, ObtainJSONWebToken

from user.api.serializer import CustomJWTSerializer

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url('^job/', TemplateView.as_view(template_name='noModelapp/home.html')),
    url(r'^api/users/', include('user.api.urls', namespace='api-users')),
    url(r'^api/auth-jwt/', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),

]
