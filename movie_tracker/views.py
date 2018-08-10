# from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from django.http import JsonResponse
from braces import views
from .models import Movie

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
