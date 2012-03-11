# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):

        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'Caros colegas,'" , 1))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'Por outro lado,'",1))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'Não podemos esquecer que'",1))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'Do mesmo modo,'",1))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'A prática mostra que'",1))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'Nunca é demais insistir que'",1))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'A experiência mostra que'",1))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'É fundamental ressaltar que'",1))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'O incentivo ao avanço tecnológico, assim como'",1))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'Assim mesmo,'",1))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'a execução deste projeto'",2))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'a complexidade dos estudos efetuados'",2))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'a atual estrutura de organização'",2))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'o novo modelo estrutural aqui preconizado'",2))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'o desenvolvimento de formas distintas de atuação'",2))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'a constante divulgação das informações'",2))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'a consolidação das estruturas'",2))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'a análise dos diversos resultados'",2))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'o início do programa de formação de atitudes'",2))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'a expansão de nossa atividade'",2))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'nos obriga à análise'",3))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'cumpre um papel essencial na formulação'",3))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'auxilia a preparação e a estruturaçào'",3))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'contribui para a correta determinação'",3))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'assume importantes posições na definição'",3))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'facilita a definição'",3))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'prejudica a percepção da importância'",3))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'oferece uma boa oportunidade de verificação'",3))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'acarreta um processo de reformulação'",3))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'exige precisão e definição'",3))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'das nossas opções de desenvolvimento futuro.'",4))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'das nossas metas financeiras e administrativas.'",4))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'das atitudes e das atribuições da diretoria.'",4))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'das novas proposições.'",4))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'das opções básicas para o sucesso do programa.'",4))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'do nosso sistema de formação de quadros.'",4))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'das condições apropriadas para os negócios.'",4))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'dos índices pretendidos.'",4))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'das formas de ação.'",4))
        db.execute("INSERT INTO generator_fragment (text, column) VALUES (%s, %d);" % ("'dos conceitos de participação geral'",4))


    def backwards(self, orm):
        
        raise RuntimeError("Cannot reverse this migration.")


    models = {
        'generator.fragment': {
            'Meta': {'object_name': 'Fragment'},
            'column': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['generator']
