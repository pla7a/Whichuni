from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

app_name = "review"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^u/$', views.uni, name='uni'),
    url(r'^s/$', views.subject, name='subject'),
    url(r'^s/(?P<subject_id>[0-9]+)/$', views.review_subject, name='review_subject'),
    url(r'^u/(?P<uni_id>[0-9]+)/$', views.review_uni, name='review_uni'),
    url(r'^us/(?P<uni_id>[0-9]+)/(?P<subject_id>[0-9]+)/$', views.review_uni_subject, name='review_uni_subject'),
]


urlpatterns += staticfiles_urlpatterns()
