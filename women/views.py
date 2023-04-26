from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Women
from rest_framework import generics, viewsets
from .serializers import WomenSerializers
from rest_framework.views import APIView

from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .permission import AdminOrUserIsAutenticated, UserIsAutenticated


class WomenListCreateApiView(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenRetrieveUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenRetrieveDelete(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers
    permission_classes = (AdminOrUserIsAutenticated,)



# class WomenViewSet(viewsets.ModelViewSet):
#     serializer_class = WomenSerializers
#
#
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return Women.objects.all()[:2]
#
#         return Women.objects.filter(pk=pk)
#
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.category})



# class WomenListApiView(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializers
#
#
# class WomenListUpdateApiView(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializers
#
#
# class WomenListDetailListApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializers
#


# class WomenApiView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializers(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Такой айди не существует'})
#         try:
#             instance = Women.objects.get(pk=pk)
#
#         except:
#             return Response({"error": 'Такой фйди не существует'})
#
#         serializer = WomenSerializers(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Такого ключа нет'})
#
#         instance = Women.objects.get(pk=pk)
#         instance.delete()
#
#         return Response({'deleted post': str(pk)})