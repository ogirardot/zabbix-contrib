from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from django.contrib import admin

from frontend.models import Contribution

admin.autodiscover()

urlpatterns += patterns('frontend.views',
    url(r'^$', login_required(index), name='home'),
    url(r'^about/?$', 'about', name='about'),
    url(r'^logout/?$', 'index', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)

# generic views
contrib_info_dict = {
    'queryset': Contribution.objects.all(),
}
contrib_cinfo_dict = {
  'form_class': ContributionForm,
  'login_required': True,
}
author_info_dict = {
    'queryset': User.objects.all(),
}

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object
urlpatterns += patterns('',
    url(r'^contrib/all/?$',
        object_list,
        contrib_info_dict,
        name="contrib_list"),
    url(r'^contrib/create/?$',
        create_object,
        contrib_cinfo_dict,
        name="contrib_create"),
    url(r'^contrib/(?P<object_id>\d+)/$',
        object_detail,
        contrib_info_dict,
        name="contrib_detail"),
    # author part :
    url(r'^author/(?P<object_id>\d+)/$',
        object_detail,
        author_info_dict,
        name="author_detail"),
)
