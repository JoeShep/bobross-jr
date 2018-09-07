from django.shortcuts import render_to_response
# For class-based stuff
from django.views.generic import View, TemplateView, ListView
from braces import views

# for function-based stuff
from django.shortcuts import get_object_or_404, render

# for both
from django.http import JsonResponse
from .models import Movie

# function-based version
def index(request):
  return render(request, 'movie_tracker/index.html')

def movies(request):
  return render(request, 'movie_tracker/movies.html')

def movie_data(request):
  movies = Movie.objects.all().values() #values can take args of the fields you want to send back
  movies_list = list(movies)  # convert the QuerySet to a list object
  return JsonResponse(movies_list, safe=False) #safe=False needed because not sending back a dict. (need to look into this)

def boring(request):
  return render(request, 'movie_tracker/boring.html')










# class-based version
class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class MoviePageView(views.JSONResponseMixin,
                    ListView):
    model = Movie

    def render_to_response(self, request, *args, **kwargs):
      print("At least this got called inside the get")
      movies = self.get_context_data()
      print("movies?", movies['object_list'])
      return self.render_json_object_response(self.get_context_data()['object_list'])
