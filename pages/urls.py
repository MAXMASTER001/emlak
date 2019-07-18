from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('about', views.about, name='about'),
  path('listings', views.listings, name='listings'),
  path('listing', views.listing, name='listing'),
  path('blogs', views.blogs, name='blogs'),
  path('blog', views.blog, name='blog'),
  path('contact', views.contact, name='contact'),
  path('elements', views.elements, name='elements'),
]