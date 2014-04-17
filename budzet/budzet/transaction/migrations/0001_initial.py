# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Transaction'
        db.create_table(u'transaction_transaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'transaction', ['Transaction'])

        # Adding model 'Product'
        db.create_table(u'transaction_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('transaction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['transaction.Transaction'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['transaction.Category'])),
        ))
        db.send_create_signal(u'transaction', ['Product'])

        # Adding model 'Category'
        db.create_table(u'transaction_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal(u'transaction', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Transaction'
        db.delete_table(u'transaction_transaction')

        # Deleting model 'Product'
        db.delete_table(u'transaction_product')

        # Deleting model 'Category'
        db.delete_table(u'transaction_category')


    models = {
        u'transaction.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'transaction.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['transaction.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['transaction.Transaction']"})
        },
        u'transaction.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['transaction']