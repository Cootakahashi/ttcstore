from django.views.generic import ListView
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from .models import store_sale
import json

class data_anotation(ListView):
    def __init__(self, query_month=None):
        self.query_month = datetime.now().month
        self.today = datetime.today()

        self.beginning_of_the_month = self.today + relativedelta(day=1)
        self.day_of_week = self.beginning_of_the_month.isoweekday()

        self.end_of_month = self.today + relativedelta(months=+1,day=1,days=-1)
        self.end_day_of_week = self.end_of_month.isoweekday()


    def __call__(self):
        # 1~7, 8~14, 15~21, 22~28, 29~31
        return "HI"

    def get_week_data(self, **kwargs):
        obj = {}
        # This week object set    
        one_week_ago = datetime.today() - timedelta(days=7)
        #this week and last week obj
        nth_week_today = datetime.today().strftime('%W')
        last_week = int(nth_week_today) - 1
        this_week_obj = store_sale.objects.filter(created_at__week=nth_week_today)
        last_week_obj = store_sale.objects.filter(created_at__week=last_week)

        #list of sale
        obj['list_sale'] = json.dumps([lis.noon_sale + lis.morning_sale for lis in this_week_obj])
        #bento sold thisweek and lastweek
        obj['bento_sold'] = json.dumps([i.sold_bento for i in this_week_obj])
        obj['last_bento_sold'] = json.dumps([i.sold_bento for i in last_week_obj])
    
        return obj


    def get_month_data(self, **kwargs):
        # 1~7, 8~14, 15~21, 22~28, 29~31
        obj = {}
        last_obj = {}
        list_sale = []
        list_sold = []
        list_sold_last = []
        index = 0
        #total_sale of each week. 0~4 as dict including sum
        for i in range(5):
            obj[i] = store_sale.objects.filter(created_at__month=self.query_month, created_at__day__range=(1+index,7+index))

            obj['list_sale',i] = sum([lis.noon_sale + lis.morning_sale for lis in obj[i]])
            # #bento sold 
            obj['sold_bento',i] = sum([i.sold_bento for i in obj[i]])
            # get last month obj and then sum
            if self.query_month == 1:
                last_obj[i] = store_sale.objects.filter(created_at__month=self.query_month+11, created_at__day__range=(1+index,7+index))
                last_obj['sold_bento',i] = sum([i.sold_bento for i in last_obj[i]])
            else:
                last_obj[i] = store_sale.objects.filter(created_at__month=self.query_month-1, created_at__day__range=(1+index,7+index))
                last_obj['sold_bento',i] = sum([i.sold_bento for i in last_obj[i]])


            index += 7

        # change to list
        for i in range(5):
            list_sale.append(obj['list_sale',i])
            list_sold.append(obj['sold_bento',i])
            list_sold_last.append(last_obj['sold_bento',i])
        obj = {}
        obj['list_sale'] = json.dumps(list_sale)
        obj['bento_sold'] = json.dumps(list_sold)
        obj['last_bento_sold'] = json.dumps(list_sold_last)
        return obj

    def get_show_integer(self, **kwargs):
        dic = {}
        # this month data from integer
        objects = store_sale.objects.filter(created_at__month=self.query_month)
        nth_week_today = datetime.today().strftime('%W')
        # for show integer
        dic['order'] = sum([i.order_bento for i in objects])
        dic['sold'] = sum([i.sold_bento for i in objects])
        dic['morning'] = sum([i.morning_sale for i in objects])
        dic['noon'] = sum([i.noon_sale for i in objects])
        dic['total'] = dic['morning'] + dic['noon']
        return dic




