from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import RequestSerializer
from .models import Request
from django.shortcuts import render
import requests
import time
import datetime

from django.http import JsonResponse


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Request.objects.all()
    serializer_class = RequestSerializer

def processedString(request):
    tic = time.clock()
    response = requests.get('http://127.0.0.1:8000/requests/?format=json')
    data = response.json()
    input_string = data[3]['string']
    string = data[3]['string'].split(data[3]['delimiter'])
    request_time = data[3]['date_created']
    id = data[3]['id']
    count = len(string)
    toc = time.clock()
    process_time = toc-tic
    response_time = datetime.datetime.now()



    return render(request, 'processedString.html', {
        'input_string' : input_string,
        'count' : count,
        'process_time' : process_time,
        'response_time' : response_time,
        'request_time' : request_time,
        'id' : id,

    })
