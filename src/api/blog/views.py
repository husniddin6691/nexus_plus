# from django.core.serializers import serialize
# from django.views.static import serve
# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import mixins

# from blog.models import Blog
# from .serializers import BlogSerializer

# class BlogGenericAPIView(GenericAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     def get(self, request):
#         books = self.get_queryset()
#         serializer = self.get_serializer(books, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serialiuzer = self.get_serializer(data=request.data)
#         if serialiuzer.is_valid():
#             serialiuzer.save()
#             return Response(serialiuzer.data, status=status.HTTP_201_CREATED)
        
#         else:
#             return Response({"data": 'invalid'}, status=status.HTTP_400_BAD_REQUEST)
        
#     def list(self):
#         pass


# class BlogGenericDetailAPIView(GenericAPIView):
#     def get(self, request, pk):
#         try:
#             blog = Blog.objects.get(pk=pk)
#             serializer = BlogSerializer(blog)
#             return Response(serializer.data)
#         except Blog.DoesNotExist:
#             return Response({"data": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
#     def put(self, request, pk):
#         try:
#             blog = Blog.objects.get(pk=pk)
#             serializer = BlogSerializer(blog, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response({"data": "invalid"}, status=status.HTTP_400_BAD_REQUEST)
#         except Blog.DoesNotExist:
#             return Response({"data": "not found"}, status=status.HTTP_404_NOT_FOUND)
        
#     def delete(self, request, pk):
#         try:
#             blog = Blog.objects.get(pk=pk)
#             blog.delete()
#             return Response({"data": "deleted"}, status=status.HTTP_204_NO_CONTENT)
#         except Blog.DoesNotExist:
#             return Response({"data": "not found"}, status=status.HTTP_404_NOT_FOUND)
        

from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from blog.models import Blog
from .serializers import BlogSerializer

class BlogGenericAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView
):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
 
    def get(self, request):
        return self.list(request)  
    
    def post(self, request):
        return self.create(request)

    


class BlogGenericDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,GenericAPIView):

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
