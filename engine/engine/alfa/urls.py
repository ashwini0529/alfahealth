from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/bmi/$', views.results, name='bmi'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/desired_id/$', views.vote, name='desired_id'),
]