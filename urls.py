from django.urls import include, path

from .views import OrderList

from django.urls import include, path

from .views import Indication_price

urlpatterns = [
    path(
        "indication_price/<int:user_id>/<int:timespan_in_days>/",
        Indication_price.as_view(),
        name="indication_price",
    ),
]