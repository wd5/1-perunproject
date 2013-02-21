from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _
from datetime import datetime


class Part(models.Model):

    # Published
    is_published = models.BooleanField(default=True)

    # Title
    title = models.CharField(_("Title"), max_length=100)

    # Content
    content = models.TextField(_("Content"), blank=True)

    # Position
    position = models.IntegerField(_("Position"), default=0)

    class Meta:
        ordering = ["position"]
        verbose_name = _("Part of training")
        verbose_name_plural = _("Parts of training")

    def __unicode__(self):
        return unicode(self.title)


class Member(models.Model):

    # Published
    is_published = models.BooleanField(default=True)

    # Title
    title = models.CharField(_("Title"), max_length=100)

    # Content
    content = models.TextField(_("Content"), blank=True)

    # Position
    position = models.IntegerField(_("Position"), default=0)

    class Meta:
        ordering = ["position"]
        verbose_name = _("Member")
        verbose_name_plural = _("Members")

    def __unicode__(self):
        return unicode(self.title)


class Skill(models.Model):

    # Published
    is_published = models.BooleanField(default=True)

    # Title
    title = models.CharField(_("Title"), max_length=100)

    # Content
    content = models.TextField(_("Content"), blank=True)

    # Position
    position = models.IntegerField(_("Position"), default=0)

    class Meta:
        ordering = ["position"]
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")

    def __unicode__(self):
        return unicode(self.title)


class Exercise(models.Model):

    # Owned
    user = models.ForeignKey(User, related_name='user')

    # Part
    part = models.ForeignKey(Part, verbose_name=_("Part"), blank=True, null=True)
    member = models.ForeignKey(Member, verbose_name=_("Member"), blank=True, null=True)
    skill = models.ForeignKey(Skill, verbose_name=_("Skill"), blank=True, null=True)

    # Published
    is_published = models.BooleanField(default=True)

    # Title
    title = models.CharField(_("Title"), max_length=100)

    # Content
    content = models.TextField(_("Content"), blank=True)

    # Structure
    structure = models.ManyToManyField("self", verbose_name=_("Structure"), blank=True, null=True)

    # Complexity (relative number value)
    complexity = models.IntegerField(_("Complexity"), default=0)

    # Position
    position = models.IntegerField(_("Position"), default=0)

    # Comments
    enable_comments = models.BooleanField(default=True)

    # TimeStamped
    date = models.DateTimeField(default=datetime.now)
    date_mod = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["part", "complexity", "title"]
        verbose_name = _("Exercise")
        verbose_name_plural = _("Exercises")

    def __unicode__(self):
        return unicode(self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('ftrainer.views.exercise_detail', [self.id])

    def simpler_queryset(self):
        return self.structure.order_by("complexity").filter(complexity__lt=self.complexity)

    def harder_queryset(self):
        return self.structure.order_by("complexity").filter(complexity__gt=self.complexity)