from django.urls import path

from nft_token.api.views import DummyView, CreateTokenView

app_name = "api"

urlpatterns = [
    path("dummy", DummyView.as_view(), name="sing_up"),
    path("tokens/create/", CreateTokenView.as_view(), name="create_token"),
]
