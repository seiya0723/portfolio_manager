from django.shortcuts import render,redirect
from django.views import View

from django.db.models import Q

from .models import Manager,Store,StoreData,Sale,SaleAmount,Access,ConversionRate
from .forms import StoreDataSearchForm,YearForm,StoreDataForm,SaleForm,SaleAmountForm,AccessForm,ConversionRateForm


import datetime

class IndexView(View):
    def get(self, request, *args, **kwargs):

        context = {}
        query   = Q()

        #店舗ごと、年ごとに集計してレンダリングする
        form    = StoreDataSearchForm(request.GET)

        if form.is_valid():
            cleaned     = form.clean()

            query &= Q(store=cleaned["store"])

            #TODO:ここで検索する時、年検索するクエリを追加して、順次appendしていく方法が早い

            #1:まずは最新と最古のデータを取り出す。
            oldest  = StoreData.objects.filter(query).order_by("date").first()
            newest  = StoreData.objects.filter(query).order_by("-date").first()

            if oldest or newest:
                newest_year = newest.date.year
                oldest_year = oldest.date.year
            else:
                today       = datetime.date.today()
                newest_year = today.year
                oldest_year = today.year


            context["store_data_list"] = []

            #2:forループで最古から最新までのデータを取り出して配列を作る。
            for year in range(oldest_year, newest_year+1):
                
                #1年分のデータをdataとする。
                data            = {}
                data["year"]    = year


                #ここでcustom_queryを元に戻す
                custom_query    = query

                custom_query &= Q(date__year=year)

                data["store_datas"]     = StoreData.objects.filter(custom_query).order_by("date")


                #1年分のデータを追加する。
                context["store_data_list"].append(data)


        #店舗IDの検索用
        context["stores"]           = Store.objects.all()

        context["sales"]            = Sale.objects.all()
        context["sale_amounts"]     = SaleAmount.objects.all()
        context["accesses"]         = Access.objects.all()
        context["conversion_rates"] = ConversionRate.objects.all()

        return render(request, "portfolio/index.html", context)

    def post(self, request, *args, **kwargs):

        form    = StoreDataForm( request.POST )

        if not form.is_valid():
            return redirect("portfolio:index")

        store_data  = form.save()


        pc_list     = request.POST.getlist("pc")
        phone_list  = request.POST.getlist("phone")
        app_list    = request.POST.getlist("app")

        
        sale                = {}
        sale["pc"]          = pc_list[0]
        sale["phone"]       = phone_list[0]
        sale["app"]         = app_list[0]
        sale["store_data"]  = store_data.id

        form    = SaleForm(sale)

        if form.is_valid():
            form.save()






        return redirect("portfolio:index")

index   = IndexView.as_view()
