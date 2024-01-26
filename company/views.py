from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Company
from .forms import Company_forms


from django.views import generic
from .models import Company
from django.core.exceptions import FieldError

class List(generic.ListView):
    model = Company
    paginate_by = 20
    
    def get_queryset(self):
        query = self.request.GET.get('query')
        ordering = self.request.GET.get('ordering', '売上高')
        order_direction = self.request.GET.get('order_direction', 'desc')

        # 昇順/降順の設定
        if order_direction == 'desc':
            ordering = '-' + ordering

        # 有効なフィールド名の確認とデフォルトのフィールド名へのフォールバック
        valid_fields = ['id', 'industry', 'pbr', 'per', 'roe', '事業内容', '会社ロゴ', '会社名', '勤続年数', '取締役報酬', '営業利益', '固定負債', '売上高', '平均年収', '平均年齢', '従業員数', '持ち株', '有形固定資産', '株価上昇率', '海外売上高比率', '粗利率', '自己資本比率']
        if ordering.lstrip('-') not in valid_fields:
            ordering = '売上高'  # 無効な場合のデフォルトフィールド

        try:
            if query:
                return Company.objects.filter(会社名__icontains=query).order_by(ordering)
            else:
                return Company.objects.all().order_by(ordering)
        except FieldError:
            # フィールドエラーが発生した場合は、デフォルトの並び替えを使用
            return Company.objects.all().order_by('売上高')
  

class Detail(generic.DetailView):
    model = Company

class Create(generic.CreateView):
    model = Company
    form_class = Company_forms
    success_url = reverse_lazy('company:list')

class Update(generic.UpdateView):
    model = Company
    form_class = Company_forms
    success_url = reverse_lazy('company:list')

class Delete(generic.DeleteView):
    model = Company
    success_url = reverse_lazy('company:list')

class Industry(generic.ListView):
    template_name = 'company/company_list.html'
    paginate_by = 20 

    def get_queryset(self):
        industry_id = self.kwargs['industry']
        query = self.request.GET.get('query')
        ordering = self.request.GET.get('ordering', '株価上昇率')  # デフォルト値 '株価上昇率'
        order_direction = self.request.GET.get('order_direction', 'desc')

        if not ordering:
            ordering = '株価上昇率'  # 空の場合はデフォルト値を設定

        if order_direction == 'asc':
            ordering = ordering
        else:
            ordering = '-' + ordering

        queryset = Company.objects.filter(industry=industry_id)

        if query:
            queryset = queryset.filter(会社名__icontains=query)

        queryset = queryset.order_by(ordering)

        return queryset
    

class Cluster(generic.ListView):
    template_name = 'company/company_list.html'
    paginate_by = 20
    
    def get_queryset(self):
        cluster_id = self.kwargs['cluster']
        ordering = self.request.GET.get('ordering', '平均年収')  
        order_direction = self.request.GET.get('order_direction', 'desc')  # デフォルトは降順

        # 昇順/降順の設定
        if order_direction == 'asc':
            ordering = ordering
        else:
            ordering = '-' + ordering

       
        return Company.objects.filter(cluster=cluster_id).order_by(ordering)
    




