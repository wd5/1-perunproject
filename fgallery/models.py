#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

#from tagging.fields import TagField
#from sorl.improved.fields import ImprovedImageWithThumbnailsField
from django.contrib.auth.models import User
from fevents.models import Event
from fgallery.managers import PublicManager

from django.conf import settings 
from PIL import Image
import os
from sorl.thumbnail.main import DjangoThumbnail


class Album(models.Model):
    author = models.ForeignKey(User)
    is_published = models.BooleanField(default=True)

    event = models.ForeignKey(Event, blank=True, null=True)

    date = models.DateTimeField(default=datetime.now)
    date_mod = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=70)
    description = models.TextField(blank=True, null=True)

    enable_comments = models.BooleanField(default=True)
    #position = models.IntegerField(default=0)
    slug = models.SlugField(max_length=70)
    #tags = TagField()

    objects = PublicManager()

    class Meta:
        verbose_name = "альбом"
        verbose_name_plural = "альбомы"

    def __unicode__(self):
        dt = unicode(self.date)[:10]
        return "[%s]-%s" % (dt, self.title)

    def images(self):
        lst = [x.image for x in self.photo_set.all().order_by('date')]
        lst = ["%s" % (x.thumbnail_tag) for x in lst]
        #lst = ["<a href='/media/%s'>%s</a>" % (x, x.split('/')[-1]) for x in lst]
        return ", <br>".join(lst)
    images.allow_tags = True

    def get_cover_image(self):
        covers = self.photo_set.filter(is_cover=True)[:1]
        if len(covers) > 0:
            image = covers[0].image
            return image
        else:
            return None

    def get_cover(self):
        covers = self.photo_set.filter(is_cover=True)[:1]
        if len(covers) > 0:
            image = covers[0].image
            thumbnail1 = DjangoThumbnail(image, (120, 120))
            return u'<img src="%s"/>' % (thumbnail1.absolute_url)
        else:
            return None
    get_cover.allow_tags = True

    @models.permalink
    def get_absolute_url(self):
        return ('fgallery.views.album1',[str(self.id)])

class Photo(models.Model):
    author = models.ForeignKey(User)
    is_published = models.BooleanField(default=True)

    album = models.ForeignKey(Album,blank=True,null=True)

    date = models.DateTimeField(default=datetime.now)
    date_mod = models.DateTimeField(auto_now=True)

    image = models.ImageField(upload_to='photos/')

    objects = PublicManager()

    """
    image = ImprovedImageWithThumbnailsField(
        upload_to='photos/',
        max_width=800, max_height=800, # Thumbnail for admin site.
        thumbnail={
            'size': (120, 120),
            #'options': ('crop','upscale'),
        },
        extra_thumbnails={
            'main': {
                'size': (200, 200),
                #'options': ('crop','upscale'),
            }
        })
    """

    description = models.TextField(blank=True, null=True)
    is_cover = models.BooleanField()
    position = models.IntegerField(default=0)

    title = models.CharField(max_length=70)
    rating = models.IntegerField(blank=True, null=True, default=0)
    view_count = models.PositiveIntegerField(default=0, editable=False)

    enable_comments = models.BooleanField(default=True)
    #slug = models.SlugField(unique=True, max_length=70, blank=True, null=True)
    #tags = TagField()

    class Meta:
        verbose_name = "фото"
        verbose_name_plural = "фотографии"

    def __unicode__(self):
        dt = unicode(self.date)[:10]
        return "%s-[%s]-%s" % (self.id, dt, self.title)

    def image_thumb(self):
        if self.image:
            thumbnail1 = DjangoThumbnail(self.image, (120, 120))
            return u'<img src="%s"/>' % (thumbnail1.absolute_url)
            #return self.image.thumbnail_tag
        else:
            return ""
    image_thumb.short_description = "Фото"
    image_thumb.allow_tags = True

    def save(self, size=(1280, 1280)):
        """
        Save Photo after ensuring it is not blank. Resize as needed.
        """
        if not self.id and not self.image:
            return

        super(Photo, self).save()

        filename = os.path.join(settings.MEDIA_ROOT,self.image.name)
        image = Image.open(filename)
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(filename, quality=95)

    def get_next_album_image(self, image):
        #previous = Photo.objects.filter(album=image.album).filter(id__lt=image.id)
        pass

    @models.permalink
    def get_absolute_url(self):
        return ('fgallery.views.photo_detail',[str(self.album.id),str(self.id)])


class Video(models.Model):
    """
       YouTube video integration
    """
    video_id = models.CharField(max_length=60)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    title = models.CharField(max_length=200, blank=True)
    event = models.ForeignKey(Event, blank=True, null=True)
    
    enable_comments = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    
    objects = PublicManager()

    def __unicode__(self):
        return "%s" % (self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('fgallery.views.video_detail',[str(self.id)])