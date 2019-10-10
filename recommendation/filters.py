from .models import Stock
import django_filters

class Stockfilter(django_filters.FilterSet):
    sector = django_filters.CharFilter(lookup_expr='icontains')
    industry = django_filters.CharFilter(lookup_expr='icontains')
    stock = django_filters.CharFilter(method='Stock')

    class Meta:
        model = Stock
        #fields = ['sector','industry', 'risk', 'csr','hr','Female_exec',]
        fields = {'sector': ['exact'],
                  'industry': ['exact'],
                  'csr':['exact']
                  }
   # def filter(self, queryset, sector, ):
