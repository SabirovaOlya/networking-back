from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ApiModel
from .serializers import ApiModelSerializer


class ApiView(APIView):
    def get(self, request):
        serializer = ApiModel.objects.all()
        serializer = ApiModelSerializer(serializer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ApiModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ApiDetail(APIView):
    def get(self, request, pk):
        serializer = ApiModelSerializer(ApiModel.objects.get(pk=pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = ApiModelSerializer(ApiModel.objects.get(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        try:
            api_model = ApiModel.objects.get(pk=pk)
        except ApiModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        api_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
