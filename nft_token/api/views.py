from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from nft_token.models import Token
from nft_token.api.serializers import CreateTokenSerializer, ListTokenSerializer
from bntm.utils import get_contract


class CreateTokenView(generics.CreateAPIView):
    model = Token
    serializer_class = CreateTokenSerializer


class TokenListView(generics.ListAPIView):
    model = Token
    serializer_class = ListTokenSerializer

    def get_queryset(self):
        return self.model.objects.all()


class SupplyView(APIView):

    def get(self, request, *args, **kwargs):
        contract = get_contract()
        return Response({"result": contract.functions.totalSupply().call()})
