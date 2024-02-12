from django.urls import path
from .views import *

urlpatterns = [
    path("say_hello/", say_hello),
    path("profile/", profile),
    path('filter_queries/<int:query_id>/', filter_queries),
    path("queries/", QueryView.as_view(), name = "query-view")

]

#retrun a json response, name: your name, email: your email,   phone_number: your phone numbe ---- write a user function and call it --------- register the view function on a path called profile.