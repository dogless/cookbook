# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recipe'
        db.create_table(u'recipe_recipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'recipe', ['Recipe'])

        # Adding model 'Step'
        db.create_table(u'recipe_step', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipe.Recipe'])),
        ))
        db.send_create_signal(u'recipe', ['Step'])


    def backwards(self, orm):
        # Deleting model 'Recipe'
        db.delete_table(u'recipe_recipe')

        # Deleting model 'Step'
        db.delete_table(u'recipe_step')


    models = {
        u'recipe.recipe': {
            'Meta': {'object_name': 'Recipe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'recipe.step': {
            'Meta': {'ordering': "('number',)", 'object_name': 'Step'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipe.Recipe']"})
        }
    }

    complete_apps = ['recipe']