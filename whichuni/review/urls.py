from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

app_name = "review"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^u/$', views.uni, name='uni'),
    url(r'^s/$', views.subject, name='subject'),
    url(r'^search/$', views.search, name='search'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^submitted/$', views.submitted, name='submitted'),
    url(r'^s/(?P<subject_id>[0-9]+)/$', views.review_subject, name='review_subject'),
    url(r'^u/(?P<uni_id>[0-9]+)/$', views.review_uni, name='review_uni'),
    url(r'^us/$', views.review_uni_subject, name='review_uni_subject'),
]


urlpatterns += staticfiles_urlpatterns()
