from datetime import date, timedelta

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from myapp1 import models


class IndicationPrice(View):
    def get(self, request, user_id, timespan_in_days) -> HttpResponse:
        client = get_object_or_404(models.Client, pk=user_id)
        timespan = timedelta(days=timespan_in_days)
        indication_price = models.Indication_price.objects.filter(customer=client).filter(
            date_ordered__gte=(date.today() - timespan)
        )

        o = []
        for indication_price in indication_price:
            products = indication_price.products.all()
            o.append({"order_data": indication_price, "products": products})

        context = {
            "client": client,
            "orders": o,
            "period": timespan_in_days,
        }
        return render(
            request=request, template_name="myapp2/indication_price.html", context=context
        )