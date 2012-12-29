from django.db import models
from django.contrib.auth.models import User


class ZabbixVersion(models.Model):
    name = models.CharField(max_length=50)
    codename = models.CharField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        if self.codename:
            return "%s (%s)" % (self.name, self.codename)
        else:
            return "%s" % (self.name)


class Product(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class ProductVersion(models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, related_name="versions")
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s" % (self.product, self.name)


class Plateform(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class PlateformVersion(models.Model):
    name = models.CharField(max_length=50)
    codename = models.CharField(max_length=250, null=True, blank=True)
    plateform = models.ForeignKey(Plateform, related_name="versions")

    def __unicode__(self):
        if self.codename:
            return "%s (%s) %s" % (self.plateform.name,
                                   self.codename, self.name)
        else:
            return "%s %s" % (self.plateform.name, self.name)


class Contribution(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    product_versions = models.ManyToManyField(ProductVersion)
    author = models.ForeignKey(User, related_name="contribs")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to="contrib_files")
    plateform_versions = models.ManyToManyField(PlateformVersion)
    zabbix_versions = models.ManyToManyField(ZabbixVersion)
    url = models.URLField(null=True, blank=True)
    documentation_url = models.URLField(null=True, blank=True)

    @property
    def zabbix(self):
        return ", ".join([version.name
                          for version in self.zabbix_versions.all()])

    @property
    def product(self):
        return self.product_versions.all()[0].product.name

    @property
    def plateform(self):
        return self.plateform_versions.all()[0].plateform.name

    @property
    def products(self):
        return "%s (%s)" % (self.product,
                            ", ".join([version.name
                                       for version
                                       in self.product_versions.all()]))

    @models.permalink
    def get_absolute_url(self):
        return ('contrib_detail', [str(self.pk)])


class ContributionPic(models.Model):
    contrib = models.ForeignKey(Contribution, related_name="pictures")
    screenshot = models.ImageField(upload_to="contrib_photo_files")
    created_at = models.DateTimeField(auto_now_add=True)


class ContributionVote(models.Model):
    contrib = models.ForeignKey(Contribution, related_name="votes")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)
    ip = models.GenericIPAddressField()
