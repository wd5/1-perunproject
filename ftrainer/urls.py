#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('ftrainer.views',
    url(r'^$', 'exercise_list', name='trainer_index'),
    url(r'^exercise/drafts/$', 'exercise_list', {'published': False}, name='trainer_exercise_drafts'),
    url(r'^exercise/add/$', view='exercise_edit', name='trainer_exercise_add'),
    url(r'^exercise/edit/(?P<pk>\d+)/$', view='exercise_edit', name='trainer_exercise_edit'),
    url(r'^exercise/(?P<pk>\d+)/$', 'exercise_detail', name='trainer_exercise_detail'),
    url(r'^part/(?P<part>\d+)/$', 'exercise_list', name='trainer_part_detail'),
    url(r'^member/(?P<member>\d+)/$', 'exercise_list', name='trainer_member_detail'),
    url(r'^skill/(?P<skill>\d+)/$', 'exercise_list', name='trainer_skill_detail'),
)
