from django.shortcuts import render
from rentandgo import settings
from zlozZamowienie.models import Zamowienie
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from zlozZamowienie.models import Zamowienie
# Create your views here.


@csrf_exempt
def payment_done(request, payment_id):
    return render(request, 'done.html')


@csrf_exempt
def payment_canceled(request, payment_id):
    return render(request, 'canceled.html')


def payment_process(request, idZamowienia):
    user = request.user
    zamowienie = Zamowienie(kupujacy=user, id=idZamowienia)

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": '%.2F' % zamowienie.do_zaplaty,
        "item_name": "Samochod",
        "invoice": str(idZamowienia),
        'currency_code': 'USD',
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return_url": request.build_absolute_uri(reverse('zamowienia:done', kwargs={'payment_id': idZamowienia})),
        "cancel_return": request.build_absolute_uri(reverse('zamowienia:canceled', kwargs={'payment_id': idZamowienia})),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, "process.html", {'idZamowienia': idZamowienia, 'form': form})


def zamowienia(request):
    zamowieniaa = Zamowienie.objects.filter(kupujacy=request.user).order_by('data_zamowienia')
    return render(request, 'zamowienia.html', {'zamowienia': zamowieniaa})


def zamowienie(request, idZamowienia):
    zamowieniee = Zamowienie.objects.get(id=idZamowienia)
    return render(request, 'zamowienie.html', {'zamowienie': zamowieniee})

