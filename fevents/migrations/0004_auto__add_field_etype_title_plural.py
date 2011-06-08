# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Etype.title_plural'
        db.add_column('fevents_etype', 'title_plural', self.gf('django.db.models.fields.CharField')(default='', max_length=70), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Etype.title_plural'
        db.delete_column('fevents_etype', 'title_plural')


    models = {
        'fevents.etype': {
            'Meta': {'ordering': "('order', 'title')", 'object_name': 'Etype'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '70', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'title_plural': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        'fevents.event': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Event'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_mod': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '70', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fevents.Etype']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fevents']
