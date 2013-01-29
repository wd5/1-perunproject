#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic.simple import direct_to_template, redirect_to
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import date_based, list_detail
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from fblog.models import Post, Ptype
from fgallery.models import Photo, Album
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
    posts = Post.objects.published()
    newsres = get_object_or_404(posts, slug=slug)
    if not request.user.is_staff:
        newsres.view_count += 1
        newsres.save()
    return direct_to_template(request,'fblog/post_detail.html', {'newsres': newsres, 'next': newsres.get_absolute_url() })

@permission_required('fblog.add_entry')
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.author = request.user
            if 'save' in request.POST:
                new_entry.is_published = True
            if 'draft' in request.POST:
                new_entry.is_published = False
            new_entry.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('blog_index'))
    else:
        form = PostForm()

    return direct_to_template(request, 'fblog/post_edit.html',{'form':form})

@permission_required('fblog.add_entry')
def add_category(request):
    if request.is_ajax():
        if request.REQUEST['title']:
            new_title = request.REQUEST['title']
            newcat = Ptype(title=new_title,title_plural=new_title,slug=new_title)
            newcat.save()
            return HttpResponse(newcat.id)
        else:
            return HttpResponse('error')

@permission_required('fblog.add_entry')
def get_album(request):
    if request.is_ajax():
        if request.REQUEST['id']:
            album_id = request.REQUEST['id']
            photos = Photo.objects.filter(album__id=album_id)
            return HttpResponse(photos)
        else:
            return HttpResponse('error')

@permission_required('fblog.change_entry')
def post_edit(request, year, month, day, slug, **kwargs):
    post = Post.objects.get(date__year=year, date__month=month, date__day=day, slug=slug)
    photos = Photo.objects.all()
    albums = Album.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.author = request.user
            if 'save' in request.POST:
                new_entry.is_published = True
            if 'draft' in request.POST:
                new_entry.is_published = False
            new_entry.save()
            form.save_m2m()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostForm(instance=post)

    return direct_to_template(request, 'fblog/post_edit.html',
        {'form':form,'post':post,'photos':photos,'albums':albums})

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

