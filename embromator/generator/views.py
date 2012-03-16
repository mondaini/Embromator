# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from embromator.generator import models
import random

class Controller():
    
    def parse_string_fragments(self, *args):
        try:
            return ' '.join(i if i is not None else '' for i in args)
        except Exception, e:
            raise e

    def parse_fragments_object(self, fragment1=models.Fragment, fragment2=models.Fragment):
        if fragment1.column != fragment2.column:
            return self.parse_string_fragments(fragment1.text, fragment2.text)
        else:
            return False

    def parse_list_fragments(self, fragments=list):
        dict_fragments = {}
        arr_fragments = []
        result = ''

        for fragment in fragments:
            dict_fragments[fragment.column] = fragment.text
        
        arr_fragments = sorted(dict_fragments)
        result = dict_fragments[1]
        arr_fragments.remove(1)
        for key in arr_fragments:
            result = ' '.join([result, dict_fragments[key]])    

        return result

    def get_random_fragments_list(self):
        lista = []
        for i in range(4):
            item = self.get_random_fragment_object(column=i+1)
            lista.append(item)
        return lista

    def get_random_fragment_object(self, column):
        lista = []
        try:
            lista = models.Fragment.objects.filter(column=column)
            item = random.randrange(0, len(lista))
            return lista[item]
        except Exception, e:
            raise e
        return

def sentences(self, request):
    controller = Controller()
    sentences_list = []
    for i in range(int(request)):
        sentences_list.append(controller.get_random_fragments_list())
    return render_to_response('embromator/home.html', {'sentences_list': sentences_list})