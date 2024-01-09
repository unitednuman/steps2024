from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import ReporterSerializer
from .models import Reporter


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# class ReporterView(generics.ListCreateAPIView):
#     permission_classes = []
#     serializer_class = ReporterSerializer
#     queryset = Reporter.objects.all()
#
#
# class ReporterDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = []
#     serializer_class = ReporterSerializer
#     queryset = Reporter.objects.all()


class ReporterView(generics.GenericAPIView):
    serializer_class = ReporterSerializer

    # def get(self,*args,**kwargs):
    #     reporters = Reporter.objects.all()
    #     serializer = self.serializer_class(reporters, many=True)
    #     return Response(serializer.data)

    def get(self, *args, **kwargs):
        reporters = Reporter.objects.all()
        paginated = self.paginate_queryset(reporters)
        serialized = self.get_serializer(paginated, many=True)
        return self.get_paginated_response(serialized.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReporterDetailView(generics.GenericAPIView):
    serializer_class = ReporterSerializer
    queryset = Reporter.objects.all()
    permission_classes = []

    def get(self, request, *args, **kwargs):
        try:
            if kwargs.get("pk"):
                data = self.queryset.get(pk=kwargs.get('pk'))
                serialized = self.get_serializer(data)
                return Response(serialized.data)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            data = self.queryset.get(pk=kwargs.get('pk'))
            serialized = self.get_serializer(data, data=request.data)
            if serialized.is_valid():
                serialized.save()
                return Response(serialized.data)
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def patch(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            data = self.queryset.get(pk=kwargs.get('pk'))
            serialized = self.get_serializer(data, data=request.data, partial=True)
            if serialized.is_valid():
                serialized.save()
                return Response(serialized.data)
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            data = self.queryset.get(pk=kwargs.get('pk'))
            data.delete()
            return Response(status= status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
