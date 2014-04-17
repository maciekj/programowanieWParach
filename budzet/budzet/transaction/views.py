from django.db.models.aggregates import Sum
from django.shortcuts import render

from django.views.generic import ListView


class TransactionsView(ListView):

    def get_queryset(self):
        queryset = super(TransactionsView, self).get_queryset()
        queryset = queryset.annotate(total=Sum('products__price')).filter(user=self.request.user)
        return queryset

