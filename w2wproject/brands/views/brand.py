from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from brands.models import Brand
from brands.serializers.brand import ExperienceUpSerializer
from accounts.models import User


class ExperienceUpView(APIView):
    def post(self, request):
        user = request.user
        data = ExperienceUpSerializer(data=request.data)
        if data.is_valid():
            point = data.validated_data.get('point', 1)
            if user.is_authenticated:
                try:
                    brand = Brand.objects.get(author=user)
                    brand.experience_up(point=point)
                    brand.save()
                    return Response({"message": "Experience updated successfully"}, status=status.HTTP_200_OK)
                except Brand.DoesNotExist:
                    return Response({"message": "Brand not found for this user"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"message": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
