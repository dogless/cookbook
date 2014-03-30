# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Ingredients'
        db.delete_table(u'recipe_ingredients')

        # Adding model 'Ingredient'
        db.create_table(u'recipe_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipe.Recipe'])),
        ))
        db.send_create_signal(u'recipe', ['Ingredient'])


    def backwards(self, orm):
        # Adding model 'Ingredients'
        db.create_table(u'recipe_ingredients', (
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipe.Recipe'])),
            ('details', self.gf('django.db.models.fields.CharField')(max_length=255)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'recipe', ['Ingredients'])

        # Deleting model 'Ingredient'
        db.delete_table(u'recipe_ingredient')


    models = {
        u'recipe.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipe.Recipe']"})
        },
        u'recipe.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'recipe.step': {
            'Meta': {'ordering': "('number',)", 'object_name': 'Step'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipe.Recipe']"})
        }
    }

    complete_apps = ['recipe']