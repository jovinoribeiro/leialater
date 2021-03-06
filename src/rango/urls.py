from rango import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name = 'add_category'),
    url(r'^add_page/(?P<category_name_url>\w+)/$', views.add_page, name = 'add_page'),
    url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name = 'user_login'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name = 'logout'),
    url(r'^login1/$', views.user_login_form, name = 'user_login_form'),
    )

