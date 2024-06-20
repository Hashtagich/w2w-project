from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from brands.models import Brand
from brands.serializers.brand import ExperienceUpSerializer, BrandSerializer, BrandModifierUpSerializer
from accounts.models import User
from rest_framework import viewsets, filters, generics, mixins
from drf_spectacular.utils import extend_schema_view, extend_schema




# class ExperienceUpView(APIView):
#     def post(self, request):
#         user = request.user
#         data = ExperienceUpSerializer(data=request.data)
#         if data.is_valid():
#             point = data.validated_data.get('point', 1)
#             if user.is_authenticated:
#                 try:
#                     brand = Brand.objects.get(author=user)
#                     brand.experience_up(point=point)
#                     brand.save()
#                     return Response({"message": "Experience updated successfully"}, status=status.HTTP_200_OK)
#                 except Brand.DoesNotExist:
#                     return Response({"message": "Brand not found for this user"}, status=status.HTTP_404_NOT_FOUND)
#             else:
#                 return Response({"message": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
#         return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema_view(
    get=extend_schema(summary='Получение бренда по его ID', tags=['Бренды'])
)
class BrandAPIRetrieve(generics.RetrieveAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


@extend_schema_view(
    get=extend_schema(summary='Получение всех брендов', tags=['Бренды'])
)
class BrandAPIList(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


@api_view(['PATCH'])
def brand_modifier_up(request, pk):
    try:
        brand = Brand.objects.get(pk=pk)
    except Brand.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = BrandModifierUpSerializer(brand, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            updated_brand_serializer = BrandSerializer(brand)
            return Response(updated_brand_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)