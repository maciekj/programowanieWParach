from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import TransactionsView
from .models import Transaction

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TransactionsView.as_view(model=Transaction, template_name="transactions.html")),
)
