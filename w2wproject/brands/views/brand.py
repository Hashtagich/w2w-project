from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from brands.models import Brand
from functools import wraps
from rest_framework import generics
from brands.serializers.brand import (BrandSerializer, BrandModifierUpSerializer, BrandLevelUpSerializer,
                                      BrandBalanceUpSerializer, BrandExperienceUpSerializer)


def get_similar_brands_decorator(func):
    """Декоратор для исключения дублирования кода в плане проверок аутентификации, нахождения бренда и т.д."""

    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        authenticated_user = request.user

        if not authenticated_user.is_authenticated:
            return Response({"error": "Пользователь не аутентифицирован"}, status=403)

        try:
            authenticated_user_brand = authenticated_user.brand

            if authenticated_user_brand:
                similar_brands = func(self, authenticated_user_brand)
                # Возвращаем список брендов согласно архитектуре сериализатора
                serializer = BrandSerializer(similar_brands, many=True)
                return Response(serializer.data)
            else:
                return Response({"error": "Для данного пользователя не найден бренд"}, status=404)

        except Exception as e:
            return Response({"error": str(e)}, status=500)

    return wrapper


@extend_schema(tags=['Бренд'])
class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

    @extend_schema(
        summary="API для получения всех по брендов кроме бренда авторизованного пользователя"
    )
    @get_similar_brands_decorator
    def list(self, authenticated_user_brand):
        return Brand.objects.all().exclude(id=authenticated_user_brand.id).distinct()



@extend_schema(
    tags=['Бренд'],
    summary="API для получения рекомендаций по брендам",
    description="Бренды, у которых совпадает хотя бы один интерес с пользователем."
)
class BrandsRecommendationsViewSet(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

    @get_similar_brands_decorator
    def list(self, authenticated_user_brand):
        brand_interests = authenticated_user_brand.interests.all()
        similar_brands = Brand.objects.filter(
            interests__in=brand_interests,
            status='accepted'
        ).exclude(id=authenticated_user_brand.id).distinct()
        return similar_brands


# @extend_schema(tags=['Бренд'])
# class BrandViewSet(viewsets.ModelViewSet):
#     serializer_class = BrandSerializer
#     queryset = Brand.objects.all()
#
#     @extend_schema(
#         summary="API для получения всех по брендов кроме бренда авторизованного пользователя"
#     )
#     def list(self, request, *args, **kwargs):
#         authenticated_user = request.user
#
#         if not authenticated_user.is_authenticated:
#             return Response({"error": "Пользователь не аутентифицирован"}, status=403)
#
#         try:
#             # Получаем бренд авторизованного пользователя
#             authenticated_user_brand = authenticated_user.brand
#
#             if authenticated_user_brand:
#                 similar_brands = Brand.objects.all().exclude(id=authenticated_user_brand.id).distinct()
#
#                 # Возвращаем список брендов согласно архитектуре сериализатора
#                 serializer = BrandSerializer(similar_brands, many=True)
#                 return Response(serializer.data)
#             else:
#                 return Response({"error": "Для данного пользователя не найден бренд"}, status=404)
#
#         except Exception as e:
#             return Response({"error": str(e)}, status=500)
#
#
# @extend_schema(
#     tags=['Бренд'],
#     summary="API для получения рекомендаций по брендам",
#     description="Бренды, у которых совпадает хотя бы один интерес с пользователем."
# )
# class BrandsRecommendationsViewSet(generics.ListAPIView):
#     serializer_class = BrandSerializer
#     queryset = Brand.objects.all()
#
#     def list(self, request, *args, **kwargs):
#         authenticated_user = request.user
#
#         if not authenticated_user.is_authenticated:
#             return Response({"error": "Пользователь не аутентифицирован"}, status=403)
#
#         try:
#             # Получаем бренд авторизованного пользователя
#             authenticated_user_brand = authenticated_user.brand
#
#             if authenticated_user_brand:
#                 # Получаем QuerySet всех интересов бренда
#                 brand_interests = authenticated_user_brand.interests.all()
#                 # Получаем QuerySet брендов, у которых совпадает хотя бы один интерес, искл-ем наш бренд и убираем дубли
#                 similar_brands = Brand.objects.filter(
#                     interests__in=brand_interests,
#                     status='accepted'
#                 ).exclude(id=authenticated_user_brand.id).distinct()
#
#                 # Преобразовываем QuerySet в обычный список значений
#                 # similar_brands_data = list(similar_brands.values())
#
#                 # Возвращаем список брендов согласно архитектуре сериализатора
#                 serializer = BrandSerializer(similar_brands, many=True)
#                 return Response(serializer.data)
#             else:
#                 return Response({"error": "Для данного пользователя не найден бренд"}, status=404)
#
#         except Exception as e:
#             return Response({"error": str(e)}, status=500)


# Реализация представлений по реализации методов бренда через наследование
class BrandUpdateView(APIView):

    def patch(self, request, pk, serializer_class):
        authenticated_user = request.user

        if not authenticated_user.is_authenticated:
            return Response({"error": "Пользователь не аутентифицирован"}, status=403)

        try:
            # Получаем бренд авторизованного пользователя
            authenticated_user_brand = authenticated_user.brand

            brand = Brand.objects.get(pk=authenticated_user_brand.id)
        except Brand.DoesNotExist:
            return Response({"error": "Бренд пользователя не найден"}, status=404)

        # Проверяем, что пользователь пытается изменить только свой бренд
        if int(pk) != authenticated_user_brand.id:
            return Response({"error": "Вы можете изменять только свой бренд"}, status=403)

        serializer = serializer_class(brand, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            updated_brand_serializer = BrandSerializer(brand)
            return Response(updated_brand_serializer.data)
        return Response({"error": "Неверный формат данных для обновления бренда"}, status=status.HTTP_400_BAD_REQUEST)


class BrandLevelUpView(BrandUpdateView):
    serializer_class = BrandLevelUpSerializer

    @extend_schema(summary="Изменение уровня бренда", tags=["Бренд"])
    def patch(self, request, pk):
        return super().patch(request, pk, self.serializer_class)


class BrandModifierUpView(BrandUpdateView):
    serializer_class = BrandModifierUpSerializer

    @extend_schema(summary="Изменение модификатора бренда", tags=["Бренд"])
    def patch(self, request, pk):
        return super().patch(request, pk, self.serializer_class)


class BrandBalanceUpView(BrandUpdateView):
    serializer_class = BrandBalanceUpSerializer

    @extend_schema(summary="Изменение баланса бренда", tags=["Бренд"])
    def patch(self, request, pk):
        return super().patch(request, pk, self.serializer_class)


class BrandExperienceUpView(BrandUpdateView):
    serializer_class = BrandExperienceUpSerializer

    @extend_schema(summary="Изменение опыта бренда", tags=["Бренд"])
    def patch(self, request, pk):
        return super().patch(request, pk, self.serializer_class)
