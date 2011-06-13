#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fgallery.models import Album, Photo, Video
from django.views.generic.simple import direct_to_template
from django.shortcuts import redirect

def albums(request):
    album_list = Album.objects.filter(is_published=True).order_by('-date_mod')
    video_list = Video.objects.published()
    return direct_to_template(request, 'fgallery/album_list.html', {'album_list': album_list, 'video_list': video_list})

def album1(request, falbum_id):
    albumres = Album.objects.get(id=falbum_id) #.all()#.order_by('-pub_date')[:10]
    return direct_to_template(request, 'fgallery/album_detail.html', {'albumres': albumres})

def album1c(request, falbum_id):
    albumres = Album.objects.get(id=falbum_id) #.all()#.order_by('-pub_date')[:10]
    return direct_to_template(request, 'fgallery/album_comments.html', {'albumres': albumres})

def photo1(request, fphoto_id):
    photores = Photo.objects.get(id=fphoto_id)
    return redirect(photores, permanent=True)

def photo_detail(request, falbum_id, fphoto_id):
    photores = Photo.objects.get(id=fphoto_id)
    if not request.user.is_staff:
        photores.view_count += 1
        photores.save()

    #previd = int(fphoto_id) - 1
    try:
        #photoprev = Photo.objects.get(id=previd)
        photoprev = photores.get_previous_by_date(album__exact=photores.album)
    except:
        photoprev = None
    if photoprev:
        if photoprev.album != photores.album:
            photoprev = None

    #nextid = int(fphoto_id) + 1
    try:
        #photonext = Photo.objects.get(id=nextid)
        photonext = photores.get_next_by_date(album__exact=photores.album)
    except:
        photonext = None
    if photonext:
        if photonext.album != photores.album:
            photonext = None

    return direct_to_template(request, 'fgallery/photo_detail.html', {'photores': photores, 'photoprev': photoprev, 'photonext': photonext})


def video_detail(request, fvideo_id):
    object = Video.objects.get(id=fvideo_id)
    return direct_to_template(request, 'fgallery/video_detail.html', {'object': object} )

def video_list(request):
    object_list = Video.objects.published()
    return direct_to_template(request, 'fgallery/video_list.html', {'object_list': object_list} )
