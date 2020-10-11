from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
     url(r'^$', views.index, name = 'home'),
     url(r'^gallery/$', views.gallery, name = 'gallery'),
     url(r'^gallery/<int:image_id>/$', views.single_image_details, name='image_details'),
     url(r'^search/', views.search_category, name = 'search_category'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)