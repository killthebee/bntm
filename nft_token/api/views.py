from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


class DummyView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"hello": "world"})
