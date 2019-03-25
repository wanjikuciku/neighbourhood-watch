from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[

    url(r'^$',views.index, name='index'),
    url(r'^signout/$',views.signout,name='signout'),
    url(r'^neighborhood/(\d+)',views.neighborhood,name='neighborhood'),
    url(r'^profile/(\d+)',views.profile,name='profile'),
    url(r'^add_business/',views.add_business,name='add_business'),
    url(r'^search/',views.search,name='search'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)