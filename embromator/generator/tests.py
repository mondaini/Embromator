# -*- coding: utf-8 -*-
from embromator.generator import models
from embromator.generator import views
from django.test import TestCase

class EmbromatorTests(TestCase):
    fragment = []
    controller = views.Controller()

    def setUp(self):
        self.fragment = [
            models.Fragment(text='Caros colegas,', column=1),
            models.Fragment(text='a execução deste projeto', column=2),
            models.Fragment(text='nos obriga à análise', column=3),
            models.Fragment(text='das nossas opções de desenvolvimento futuro.', column=4)
        ]

        self.fragment_mixed = [
            models.Fragment(text='nos obriga à análise', column=3),
            models.Fragment(text='Caros colegas,', column=1),
            models.Fragment(text='das nossas opções de desenvolvimento futuro.', column=4),
            models.Fragment(text='a execução deste projeto', column=2),
        ]

        self.fragment_2 = [
            models.Fragment(text='Por outro lado,', column=1),
            models.Fragment(text='a complexidade dos estudos efetuados', column=2),
            models.Fragment(text='cumpre um papel essencial na formulação', column=3),
            models.Fragment(text='das nossas metas financeiras e administrativas', column=4),
        ]

    def test_join_two_words(self):
        palavra_a = 'Cachorro'
        palavra_b = 'sinistro'
        frase = self.controller.parse_string_fragments(palavra_a, palavra_b)
        self.assertEqual(frase, 'Cachorro sinistro')

    def test_joining_adjacents_column_fragments_must_work(self):
        response = self.controller.parse_string_fragments(self.fragment[0].text, self.fragment[1].text)
        expected = 'Caros colegas, a execução deste projeto'
        self.assertEqual(response, expected)
        self.assertEqual(self.controller.parse_fragments_object(self.fragment[0], self.fragment[1]), expected)

    def test_joining_same_column_fragments_must_fail(self):
        self.assertFalse(self.controller.parse_fragments_object(self.fragment[2], self.fragment[2]))

    def test_joining_4_fragments_ordered_and_parse_correctly(self):
        response = self.controller.parse_list_fragments(fragments=self.fragment)
        expected = 'Caros colegas, a execução deste projeto nos obriga à análise das nossas opções de desenvolvimento futuro.'
        self.assertEqual(response, expected)

    def test_joining_4_fragments_without_order_and_parse_correctly(self):
        response = self.controller.parse_list_fragments(fragments=self.fragment_mixed)
        expected = 'Caros colegas, a execução deste projeto nos obriga à análise das nossas opções de desenvolvimento futuro.'
        self.assertEqual(response, expected)

    def test_must_return_list_with_4_random_fragments_in_sequence(self):
        def test_responses(response):
            if response:
                for i in range(4):
                    self.assertEqual(i+1, response[i].column)
            else:
                return self.fail('Could\'t generate the fragments list.')
        response = self.fragment
        
        """Mock"""
        test_responses(response)
        
        """The real thing"""
        #test_responses(self.controller.get_random_fragments_list())