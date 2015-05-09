from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Work_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url (r'^$', 'TasksManager.index.page'),
	url (r'^home$', 'TasksManager.index.home'),
	url (r'^createinstance$', 'TasksManager.index.createinstance'),
	url (r'^confirmation$', 'TasksManager.index.confirmation'),
)
