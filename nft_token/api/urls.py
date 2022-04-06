from django.urls import path

from nft_token.api.views import SupplyView, CreateTokenView, TokenListView

app_name = "api"

urlpatterns = [
    path("tokens/total_supply/", SupplyView.as_view(), name="total_supply"),
    path("tokens/create/", CreateTokenView.as_view(), name="create_token"),
    path("tokens/list/", TokenListView.as_view(), name="token_list"),
]
