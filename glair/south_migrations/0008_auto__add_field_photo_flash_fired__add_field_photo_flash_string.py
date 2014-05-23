# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Photo.flash_fired'
        db.add_column(u'glair_photo', 'flash_fired',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Photo.flash_string'
        db.add_column(u'glair_photo', 'flash_string',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Photo.flash_fired'
        db.delete_column(u'glair_photo', 'flash_fired')

        # Deleting field 'Photo.flash_string'
        db.delete_column(u'glair_photo', 'flash_string')


    models = {
        u'glair.camera': {
            'Meta': {'object_name': 'Camera'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'glair.make': {
            'Meta': {'object_name': 'Make'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'glair.photo': {
            'Meta': {'object_name': 'Photo'},
            'camera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['glair.Camera']", 'null': 'True'}),
            'exposure_program': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'exposure_time': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'flash_fired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flash_string': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'fnumber': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1'}),
            'focal_length': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'iso_speed': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'make': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['glair.Make']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'taken_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        }
    }

    complete_apps = ['glair']