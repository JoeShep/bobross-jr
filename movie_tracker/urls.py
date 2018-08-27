from django.conf.urls import url
from movie_tracker import views

urlpatterns = [
    # function-based version
    url(r'^$', views.index, name='home'),
    url(r'^movies/$', views.movies, name='movies'),
    url(r'^movie_data/$', views.movie_data, name='movie_data'),
    # class-based version
    # url(r'^$', views.HomePageView.as_view(), name='home'),
    # url(r'^about/$', views.AboutPageView.as_view(), name='about'),
]
