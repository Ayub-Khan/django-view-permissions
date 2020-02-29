from django.conf.urls import url

from django_view_permissions.tests.test_app import views


urlpatterns = [
    url(r'^test', views.test, name='test'),
]
