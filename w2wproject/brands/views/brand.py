from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from brands.models import Brand
from brands.serializers.brand import (BrandSerializer, BrandModifierUpSerializer, BrandLevelUpSerializer,
                                      BrandBalanceUpSerializer, BrandExperienceUpSerializer)
from accounts.models import User
from rest_framework import viewsets, filters, generics, mixins
from drf_spectacular.utils import extend_schema_view, extend_schema


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


@extend_schema(
    summary="Изменение модификатора бренда",
    tags=["Бренды"]
)
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


@extend_schema(
    summary="Изменение уровня бренда",
    tags=["Бренды"]
)
@api_view(['PATCH'])
def brand_level_up(request, pk):
    try:
        brand = Brand.objects.get(pk=pk)
    except Brand.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = BrandLevelUpSerializer(brand, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            updated_brand_serializer = BrandSerializer(brand)
            return Response(updated_brand_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandLevelUpView(APIView):
    serializer_class = BrandLevelUpSerializer

    @extend_schema(summary="Изменение уровня бренда", tags=["Бренды"])
    def patch(self, request, pk):
        try:
            brand = Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BrandLevelUpSerializer(brand, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            updated_brand_serializer = BrandSerializer(brand)
            return Response(updated_brand_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandModifierUpView(APIView):
    serializer_class = BrandModifierUpSerializer

    @extend_schema(summary="Изменение модификатора бренда", tags=["Бренды"])
    def patch(self, request, pk):
        try:
            brand = Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BrandModifierUpSerializer(brand, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            updated_brand_serializer = BrandSerializer(brand)
            return Response(updated_brand_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandBalanceUpView(APIView):
    serializer_class = BrandBalanceUpSerializer

    @extend_schema(summary="Изменение баланса бренда", tags=["Бренды"])
    def patch(self, request, pk):
        try:
            brand = Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BrandBalanceUpSerializer(brand, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            updated_brand_serializer = BrandSerializer(brand)
            return Response(updated_brand_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandExperienceUpView(APIView):
    serializer_class = BrandExperienceUpSerializer

    @extend_schema(summary="Изменение опыта бренда", tags=["Бренды"])
    def patch(self, request, pk):
        try:
            brand = Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BrandExperienceUpSerializer(brand, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            updated_brand_serializer = BrandSerializer(brand)
            return Response(updated_brand_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# наследование (в разработке)
# class BrandUpdateView(APIView):
#
#     def patch(self, request, pk, serializer_class):
#         try:
#             brand = Brand.objects.get(pk=pk)
#         except Brand.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         serializer = serializer_class(brand, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             updated_brand_serializer = BrandSerializer(brand)
#             return Response(updated_brand_serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BrandLevelUpView(BrandUpdateView):
#     serializer_class = BrandLevelUpSerializer
#
#     @extend_schema(summary="Изменение уровня бренда", tags=["Бренды"])
#     def patch(self, request, pk):
#         super().patch(request, pk, self.serializer_class)
#
#
# class BrandModifierUpView(BrandUpdateView):
#     serializer_class = BrandModifierUpSerializer
#
#     @extend_schema(summary="Изменение модификатора бренда", tags=["Бренды"])
#     def patch(self, request, pk):
#         super().patch(request, pk, self.serializer_class)


# class BrandBalanceUpView(BrandUpdateView):
#     serializer_class = BrandBalanceUpSerializer
#
#     @extend_schema(summary="Изменение баланса бренда", tags=["Бренды"])
#     def patch(self, request, pk):
#         super().patch(request, pk, self.serializer_class)

# class BrandExperienceUpView(BrandUpdateView):
#     serializer_class = BrandExperienceUpSerializer
#
#     @extend_schema(summary="Изменение опыта бренда", tags=["Бренды"])
#     def patch(self, request, pk):
#         super().patch(request, pk, self.serializer_class)
