from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    # /app/
    url( r'^$' , views.index, name='index' ) ,

    # /app/<album_id>/
    url( r'^(?P<album_id>[0-9]+)/$', views.detail , name='detail' ) ,

    # /app/<album_id>/favorite/
    url( r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite' ) ,
]

if settings.DEBUG:
    urlpatterns+=static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
