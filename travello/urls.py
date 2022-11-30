from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name='about'),
    path("worker", views.worker, name="worker"),
    path("contact", views.contact, name='contact'),
    path("book", views.book, name='book'),
    path("carpenter", views.carpenter, name='carpenter'),
    path("electrician", views.electrician, name='electrician'),
    path("plumber", views.plumber, name='plumber'),
    path("salonmen", views.salonmen, name='salonmen'),
    path("salonwomen", views.salonwomen, name='salonwomen'),
    path("spawomen", views.spawomen, name='spawomen')
]
