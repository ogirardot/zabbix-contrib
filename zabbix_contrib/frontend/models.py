from django.db import models
from django.contrib.auth.models import User


class ZabbixVersion(models.Model):
    name = models.CharField(max_length=50)
    codename = models.CharField(max_length=250, null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


class ProductVersion(models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, related_name="versions")
    created_at = models.DateTimeField(auto_now_add=True)


class Plateform(models.Model):
    name = models.CharField(max_length=50)


class PlateformVersion(models.Model):
    name = models.CharField(max_length=50)
    codename = models.CharField(max_length=250, null=True, blank=True)


class Contribution(models.Model):
    name = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name="contribs")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to="contrib_files")
    plateform = models.ForeignKey(Plateform, related_name="contribs")
    url = models.URLField(null=True, blank=True)
    documentation_url = models.URLField(null=True, blank=True)


class ContributionPic(models.Model):
    contrib = models.ForeignKey(Contribution, related_name="pictures")
    screenshot = models.ImageField(upload_to="contrib_photo_files")
    created_at = models.DateTimeField(auto_now_add=True)


class ContributionVote(models.Model):
    contrib = models.ForeignKey(Contribution, related_name="votes")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)
    ip = models.GenericIPAddressField()
