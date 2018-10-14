from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # /app/
    url( r'^$' , views.IndexView.as_view( ) , name='index' ) ,

    # /app/register

    url( r'^register/$' , views.UserForm.as_view( ) , name='register' ) ,

    # /app/<album_id>/
    url( r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view( ) , name='detail' ) ,

    # /app/album/add/
    url( r'album/add/$' , views.AlbumCreate.as_view( ) , name='album-add' ) ,

    # /app/album/2/
    url( r'album/(?P<pk>[0-9]+)/$' , views.AlbumUpdate.as_view( ) , name='album-update' ) ,

    # /app/album/2/delete
    url( r'album/(?P<pk>[0-9]+)/delete/$' , views.AlbumDelete.as_view( ) , name='album-delete' ) ,


]

if settings.DEBUG:
    urlpatterns+=static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
