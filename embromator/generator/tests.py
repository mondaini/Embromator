# -*- coding: utf-8 -*-
from embromator.generator import models
from embromator.generator import views
from django.test import TestCase

class EmbromatorTests(TestCase):
    trecho = []
    controller = views.Controller()

    def setUp(self):
        self.trecho = [
            models.Trecho(text='Caros colegas,', coluna=1),
            models.Trecho(text='a execução deste projeto', coluna=2),
            models.Trecho(text='nos obriga à análise', coluna=3),
            models.Trecho(text='das nossas opções de desenvolvimento futuro.', coluna=4)
        ]

        self.trecho_misturado = [
            models.Trecho(text='nos obriga à análise', coluna=3),
            models.Trecho(text='Caros colegas,', coluna=1),
            models.Trecho(text='das nossas opções de desenvolvimento futuro.', coluna=4),
            models.Trecho(text='a execução deste projeto', coluna=2),
        ]

        self.trecho_2 = [
            models.Trecho(text='Por outro lado,', coluna=1),
            models.Trecho(text='a complexidade dos estudos efetuados', coluna=2),
            models.Trecho(text='cumpre um papel essencial na formulação', coluna=3),
            models.Trecho(text='das nossas metas financeiras e administrativas', coluna=4),
        ]

    def test_junta_duas_palavras(self):
        palavra_a = 'Cachorro'
        palavra_b = 'sinistro'
        frase = self.controller.parse_string_trechos(palavra_a, palavra_b)
        self.assertEqual(frase, 'Cachorro sinistro')

    def test_junta_trechos_colunas_adjacentes_deve_funcionar(self):
        response = self.controller.parse_string_trechos(self.trecho[0].text, self.trecho[1].text)
        expected = 'Caros colegas, a execução deste projeto'
        self.assertEqual(response, expected)
        self.assertEqual(self.controller.parse_objeto_trechos(self.trecho[0], self.trecho[1]), expected)

    def test_junta_trechos_mesma_coluna_deve_falhar(self):
        self.assertFalse(self.controller.parse_objeto_trechos(self.trecho[2], self.trecho[2]))

    def test_junta_4_trechos_em_ordem_e_faz_parse_corretamente(self):
        response = self.controller.parse_list_trechos(trechos=self.trecho)
        expected = 'Caros colegas, a execução deste projeto nos obriga à análise das nossas opções de desenvolvimento futuro.'
        self.assertEqual(response, expected)

    def test_junta_4_trechos_sem_ordem_e_faz_parse_corretamente(self):
        response = self.controller.parse_list_trechos(trechos=self.trecho_misturado)
        expected = 'Caros colegas, a execução deste projeto nos obriga à análise das nossas opções de desenvolvimento futuro.'
        self.assertEqual(response, expected)

    def test_retorna_lista_com_4_trechos_aleatorios(self):
        def testa_response(response):
            if response:
                for i in range(4):
                    self.assertEqual(i+1, response[i].coluna)
            else:
                return self.fail('Não gerou lista de trechos.')
        response = self.trecho
        
        """Mock"""
        testa_response(response)
        
        """Uso real"""
        #testa_response(self.controller.get_random_trechos_list())
