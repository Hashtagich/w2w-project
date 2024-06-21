from django.views import View
from yookassa import Configuration, Payment
from django.conf import settings
from .models import Tariff
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import uuid

class YookassaPayment(View):
    def get(self, request, pk):
        Configuration.account_id = settings.YOOKASSA_SHOP_ID
        Configuration.secret_key = settings.YOOKASSA_SECRET_KEY

        tariff = get_object_or_404(Tariff, pk=pk)
        price = tariff.price
        name = tariff.name


        payment = Payment.create({
            "amount": {
                "value": f"{price}.00",
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "http://127.0.0.1:8000/"
            },
            "capture": True,
            "description": f'Оплата тарифа {name}'
        }, uuid.uuid4())
        return HttpResponseRedirect(payment.confirmation.confirmation_url)
