# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Camera'
        db.create_table(u'glair_camera', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'glair', ['Camera'])

        # Adding model 'Make'
        db.create_table(u'glair_make', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'glair', ['Make'])

        # Adding field 'Photo.make'
        db.add_column(u'glair_photo', 'make',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['glair.Make']),
                      keep_default=False)

        # Adding field 'Photo.camera'
        db.add_column(u'glair_photo', 'camera',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['glair.Camera']),
                      keep_default=False)

        # Adding field 'Photo.iso_speed'
        db.add_column(u'glair_photo', 'iso_speed',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Camera'
        db.delete_table(u'glair_camera')

        # Deleting model 'Make'
        db.delete_table(u'glair_make')

        # Deleting field 'Photo.make'
        db.delete_column(u'glair_photo', 'make_id')

        # Deleting field 'Photo.camera'
        db.delete_column(u'glair_photo', 'camera_id')

        # Deleting field 'Photo.iso_speed'
        db.delete_column(u'glair_photo', 'iso_speed')


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
            'camera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['glair.Camera']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'iso_speed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'make': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['glair.Make']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['glair']