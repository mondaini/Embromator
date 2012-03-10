# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Trecho'
        db.create_table('generator_trecho', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('coluna', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('generator', ['Trecho'])


    def backwards(self, orm):
        
        # Deleting model 'Trecho'
        db.delete_table('generator_trecho')


    models = {
        'generator.trecho': {
            'Meta': {'object_name': 'Trecho'},
            'coluna': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['generator']
