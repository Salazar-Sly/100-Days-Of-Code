from django.conf.urls import url
from . import views 

app_name = 'refer'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="details"),
    url(r'refer/add/$', views.ReferralCreate.as_view(), name='referral-add'),
]