from webbrowser import get
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
# Create your views here.


def say_hello(request):
    return HttpResponse("<h1>Hello Fleur</h1>")

def profile(request):
    profile =  {"name": "Roy Mohubu", 
                 "number": 74689264, 
                 "email": "roy.mohubu@gmail.com"}
    return JsonResponse(profile)

#1. Write a view function called filter_queries
#1.a The view function should receive query_id througn the url
#2. Return a JsonResponse datta with the following data: Id, title, description, status,  and submmitted_by#1.c the id should be received throuh the url

def filter_queries (request, query_id):
    # query = get(id=query_id)
    data = {
        "Id": query_id,
        "title": "This one",
        "description": "This is a description of my choice",
        "status": "Pending",
        "submitted_by":  "Sylvia"

    }
    return JsonResponse(data)


class QueryView(View):
    
    queries = [
        {"id": 1, "title": "Adama declined val shots"},
        {"id": 2, "title": "Samson declined Val shots"}]

    def get(self, request):
        
        return JsonResponse({"result": self.queries})
    
    def post(self, request):

        return JsonResponse({"Status": "ok"})