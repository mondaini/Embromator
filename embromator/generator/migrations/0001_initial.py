# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Fragment'
        db.create_table('generator_fragment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('column', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('generator', ['Fragment'])


    def backwards(self, orm):
        
        # Deleting model 'Fragment'
        db.delete_table('generator_fragment')


    models = {
        'generator.fragment': {
            'Meta': {'object_name': 'Fragment'},
            'column': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['generator']
