from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import store_sale
import json
from datetime import datetime, timedelta
from .get_date import data_anotation
from django.contrib.auth.views import LoginView
from django.contrib import messages

def helloworld(request):
    return HttpResponse('hello')

def get_nth_week(day):
    return (day - 1) // 7 + 1


def post(request):
    if request.method == 'POST':
        user = request.user
        morning_sale = request.POST['morning_sale']
        noon_sale = request.POST['noon_sale']
        order_bento = request.POST['order_bento']
        sold_bento = request.POST['sold_bento']
        payment = request.POST['payment']
        object = store_sale.objects.create(user=user, morning_sale=morning_sale,
        noon_sale=noon_sale, order_bento=order_bento,
        sold_bento=sold_bento, payment=payment)
        object.save()
        if user == 'sheine' or user == 'mo':
            return render(request, 'success.html')
        else:
            response = redirect('/all/')
            return response
    else:
        return render(request, 'post.html')

#query検索なし 今週の値
#query検索あり 今月の値
#user sheine and mo 弁当の値 
#user sheine and mo classadd none to sales


class graphList(ListView):
    model = store_sale
    context_object_name = 'objects'
    template_name = "all.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query_month = self.request.GET.get('created_at')
        if query_month:
            context['all'] = store_sale.objects.filter(created_at__month=query_month)
        else:
            this_month = datetime.now().month
            context['all'] = store_sale.objects.filter(created_at__month=this_month)
        inst = data_anotation(query_month)
        inst()
        context['int'] = inst.get_show_integer()
        if query_month:
            context['obj'] = inst.get_month_data()
            context['tag'] = json.dumps(['1週目', '2週目', '3週目', '4週目', '5週目'])

        else:
            context['obj'] = inst.get_week_data()
            context['tag'] = json.dumps(['月曜', '火曜', '水曜', '木曜', '金曜', '土曜'])

        return context


class Login(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        messages.success(self.request, 'You success login!')
        return super().form_valid(form)
    
    def forminvalid(self, form):
        messages.error(self.request, 'You can not login.')
        return super().form_invalid(form)


