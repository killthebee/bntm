from django.urls import path

from nft_token.api.views import DummyView

app_name = "api"

urlpatterns = [
    path("dummy", DummyView.as_view(), name="sing_up"),
]
