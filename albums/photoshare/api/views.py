from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)

class UserListView(generics.ListAPIView):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Photo.objects.all()
        user = self.request.user
        customer = Customer.objects.get(user=user)
        get_params = self.request.query_params.get('search')
        if get_params is None:
            queryset = queryset.filter(category__customer=customer)
        else:
            queryset = queryset.filter(category__name=get_params)
        return queryset


@api_view(['DELETE'])
def photoDelete(request, pk):
    photo = Photo.objects.get(id=pk)
    photo.delete()
    return Response("Item success fully")
    