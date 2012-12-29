from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from django.contrib import admin

from frontend.models import Contribution
from frontend.forms import ContributionForm

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^accounts/', include('accounts.urls')),
)

urlpatterns += patterns('frontend.views',
    url(r'^$', 'index', name='home'),
    url(r'^about/?$', 'about', name='about'),
)

# generic views
contrib_info_dict = {
    'queryset': Contribution.objects.all(),
}
contrib_cinfo_dict = {
  'form_class': ContributionForm,
  'login_required': False,
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
)
