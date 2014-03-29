# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Step.details'
        db.add_column(u'recipe_step', 'details',
                      self.gf('django.db.models.fields.CharField')(default='a', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Step.details'
        db.delete_column(u'recipe_step', 'details')


    models = {
        u'recipe.recipe': {
            'Meta': {'object_name': 'Recipe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'recipe.step': {
            'Meta': {'ordering': "('number',)", 'object_name': 'Step'},
            'details': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recipe.Recipe']"})
        }
    }

    complete_apps = ['recipe']