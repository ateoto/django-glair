# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Photo.exposure_time'
        db.alter_column(u'glair_photo', 'exposure_time', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Photo.fnumber'
        db.alter_column(u'glair_photo', 'fnumber', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Photo.taken_on'
        db.alter_column(u'glair_photo', 'taken_on', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Photo.exposure_program'
        db.alter_column(u'glair_photo', 'exposure_program', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True))

        # Changing field 'Photo.iso_speed'
        db.alter_column(u'glair_photo', 'iso_speed', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'Photo.camera'
        db.alter_column(u'glair_photo', 'camera_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['glair.Camera'], null=True))

        # Changing field 'Photo.focal_length'
        db.alter_column(u'glair_photo', 'focal_length', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Photo.make'
        db.alter_column(u'glair_photo', 'make_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['glair.Make'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Photo.exposure_time'
        raise RuntimeError("Cannot reverse this migration. 'Photo.exposure_time' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Photo.exposure_time'
        db.alter_column(u'glair_photo', 'exposure_time', self.gf('django.db.models.fields.CharField')(max_length=20))

        # User chose to not deal with backwards NULL issues for 'Photo.fnumber'
        raise RuntimeError("Cannot reverse this migration. 'Photo.fnumber' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Photo.fnumber'
        db.alter_column(u'glair_photo', 'fnumber', self.gf('django.db.models.fields.CharField')(max_length=20))

        # User chose to not deal with backwards NULL issues for 'Photo.taken_on'
        raise RuntimeError("Cannot reverse this migration. 'Photo.taken_on' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Photo.taken_on'
        db.alter_column(u'glair_photo', 'taken_on', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Photo.exposure_program'
        db.alter_column(u'glair_photo', 'exposure_program', self.gf('django.db.models.fields.PositiveSmallIntegerField')())

        # Changing field 'Photo.iso_speed'
        db.alter_column(u'glair_photo', 'iso_speed', self.gf('django.db.models.fields.PositiveIntegerField')())

        # User chose to not deal with backwards NULL issues for 'Photo.camera'
        raise RuntimeError("Cannot reverse this migration. 'Photo.camera' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Photo.camera'
        db.alter_column(u'glair_photo', 'camera_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['glair.Camera']))

        # User chose to not deal with backwards NULL issues for 'Photo.focal_length'
        raise RuntimeError("Cannot reverse this migration. 'Photo.focal_length' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Photo.focal_length'
        db.alter_column(u'glair_photo', 'focal_length', self.gf('django.db.models.fields.CharField')(max_length=20))

        # User chose to not deal with backwards NULL issues for 'Photo.make'
        raise RuntimeError("Cannot reverse this migration. 'Photo.make' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Photo.make'
        db.alter_column(u'glair_photo', 'make_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['glair.Make']))

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
            'fnumber': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
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