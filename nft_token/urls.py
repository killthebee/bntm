from django.urls import path, include

app_name = "nft_token"

urlpatterns = [
    path("api/", include("nft_token.api.urls", namespace="nft_token_api")),
]