# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Photo.edited_on'
        db.delete_column(u'glair_photo', 'edited_on')

        # Deleting field 'Photo.owner'
        db.delete_column(u'glair_photo', 'owner_id')

        # Deleting field 'Photo.uploaded_on'
        db.delete_column(u'glair_photo', 'uploaded_on')

        # Deleting field 'Photo.private'
        db.delete_column(u'glair_photo', 'private')

        # Deleting field 'Photo.slug'
        db.delete_column(u'glair_photo', 'slug')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Photo.edited_on'
        raise RuntimeError("Cannot reverse this migration. 'Photo.edited_on' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Photo.edited_on'
        db.add_column(u'glair_photo', 'edited_on',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Photo.owner'
        raise RuntimeError("Cannot reverse this migration. 'Photo.owner' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Photo.owner'
        db.add_column(u'glair_photo', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Photo.uploaded_on'
        raise RuntimeError("Cannot reverse this migration. 'Photo.uploaded_on' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Photo.uploaded_on'
        db.add_column(u'glair_photo', 'uploaded_on',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Photo.private'
        db.add_column(u'glair_photo', 'private',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Photo.slug'
        raise RuntimeError("Cannot reverse this migration. 'Photo.slug' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Photo.slug'
        db.add_column(u'glair_photo', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=50),
                      keep_default=False)


    models = {
        u'glair.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['glair']