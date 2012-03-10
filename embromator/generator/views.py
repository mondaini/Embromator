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
        dict_trechos = {}
        arr_trechos = []
        result = ''

        for trecho in trechos:
            dict_trechos[trecho.coluna] = trecho.text
        
        arr_trechos = sorted(dict_trechos)
        result = dict_trechos[1]
        arr_trechos.remove(1)
        for key in arr_trechos:
            result = ' '.join([result, dict_trechos[key]])    

        return result