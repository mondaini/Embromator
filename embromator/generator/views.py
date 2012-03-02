# -*- coding: utf-8 -*-
from embromator.generator import models

class Controller():
    
    def parse_string_trechos(self, *args):
        try:
            return ' '.join(i if i is not None else '' for i in args)
        except Exception, e:
            raise e

    def parse_objeto_trechos(self, trecho1=models.Trecho, trecho2=models.Trecho):
        if trecho1.coluna != trecho2.coluna:
            return self.parse_string_trechos(trecho1.text, trecho2.text)
        else:
            return False

    def parse_list_trechos(self, trechos=list):
        # for trecho in list:
        return True
