from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiview(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Return a list of APIView feature."""

        an_apiview =  [
            'Uses HTTP methods a function(get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped maunally to URLS'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})