from store.api.serializers import ProductListSerializers
from rest_framework import generics, mixins
from store.models import Product
from .serializers import ProductListSerializers

class ProductListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = ProductListSerializers

    def get_queryset(self):
        return Product.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create( request, *args, **kwargs)
    
    
class ProductAPIRUDView(generics.RetrieveDestroyAPIView):
    lookup_field = 'slug'
    serializer_class = ProductListSerializers

    def get_queryset(self):
        return Product.objects.all()
    
    
    def patch(self, request, *args, **kwargs):
        return self.update( request, *args, **kwargs)
    