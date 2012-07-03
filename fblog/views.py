#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic.simple import direct_to_template, redirect_to
from django.shortcuts import redirect
from django.views.generic import date_based, list_detail
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from fblog.models import Post, Ptype
from fblog.forms import PostForm
import datetime, time

def post_list(request, page=0, template_name='fblog/post_list.html', **kwargs):
    return list_detail.object_list(
        request,
        queryset = Post.objects.published(),
        paginate_by = 10,
        page = page,
        template_name = template_name,
        **kwargs)

def news1(request, fnews_id):
    """ backward compatible, deprecated """
    newsres = Post.objects.get(id=fnews_id)
    return redirect(newsres, permanent=True)
    #return direct_to_template(request,'fblog/post_detail.html', {'newsres':newsres})

def post_detail(request, year, month, day, slug, **kwargs):
    newsres = Post.objects.get(slug=slug)
    if not request.user.is_staff:
        newsres.view_count += 1
        newsres.save()
    return direct_to_template(request,'fblog/post_detail.html', {'newsres': newsres, 'next': newsres.get_absolute_url() })

def post_archive_year(request, year, page=0, template_name='fblog/post_archive_year.html', **kwargs):
    return list_detail.object_list(
        request,
        queryset = Post.objects.published().filter(date__year=year).order_by('-date',),
        paginate_by = 5,
        page = page,
        template_name = template_name,
        extra_context = {'year':year},
        **kwargs)

def post_archive_month(request, year, month, page=0, template_name='fblog/post_archive_month.html', **kwargs):
    return list_detail.object_list(
        request,
        queryset = Post.objects.published().filter(date__year=year, date__month=month).order_by('-date',),
        paginate_by = 5,
        page = page,
        template_name = template_name,
        extra_context = {'month':datetime.date(int(year),int(month),1)},
        **kwargs)

def post_archive_day(request, year, month, day, page=0, template_name='fblog/post_list.html', **kwargs):
    return list_detail.object_list(
        request,
        queryset = Post.objects.published().filter(date__year=year, date__month=month, date__day=day).order_by('-date',),
        paginate_by = 5,
        page = page,
        template_name = template_name,
        **kwargs)

def category_detail(request, slug, page=0, template_name='fblog/post_list.html', **kwargs):
    category = Ptype.objects.get(slug=slug)
    return list_detail.object_list(
        request,
        queryset = Post.objects.published().filter(type__slug__exact=slug),
        paginate_by = 10,
        page = page,
        template_name = template_name,
        extra_context = {'category':category.title_plural},
        **kwargs)

@permission_required('fblog.add_entry')
def post_new(request, **kwargs):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.author = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('blog_index'))
    else:
        form = PostForm()

    return direct_to_template(request, 'fblog/post_edit.html',{'form':form})

@permission_required('fblog.change_entry')
def post_edit(request, year, month, day, slug, **kwargs):
    post = Post.objects.get(date__year=year, date__month=month, date__day=day, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm(instance=post)

    return direct_to_template(request, 'fblog/post_edit.html',{'form':form,'post':post})
