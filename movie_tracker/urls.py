from django.conf.urls import url
from movie_tracker import views

urlpatterns = [
    # Notice the URL has been named
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^movies/$', views.MoviePageView.as_view(), name='movies'),
]
