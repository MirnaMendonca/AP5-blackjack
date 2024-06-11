import unittest
from unittest.mock import patch
from io import StringIO
import sys
from blackjack import *

class TestBlackjack(unittest.TestCase):

    def test_criar_baralho_tamanho(self):
        baralho = criar_baralho()
        self.assertEqual(len(baralho), 52)

    def test_criar_baralho_cartas_estao_corretas(self):
        baralho = criar_baralho()
        self.assertTrue(all(carta in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] for carta in baralho))

    def test_calcular_pontuacao_mao_vazia(self):
        mao = []
        pontuacao = calcular_pontuacao(mao)
        self.assertEqual(pontuacao, 0)
    
    def test_calcular_pontuacao_mao_um_as(self):
        mao = ['A']
        pontuacao = calcular_pontuacao(mao)
        self.assertEqual(pontuacao, 11)

    def test_calcular_pontuacao_mao_dois_ases(self):
        mao = ['A', 'A']
        pontuacao = calcular_pontuacao(mao)
        self.assertEqual(pontuacao, 12)
    
    def test_calcular_pontuacao_mao_tres_figuras(self):
        mao = ['J', 'Q', 'K']
        pontuacao = calcular_pontuacao(mao)
        self.assertEqual(pontuacao, 30)
    
    @patch('blackjack.criar_baralho', return_value=['K', 'Q', '2', '3', 'J'])
    @patch('builtins.input', side_effect=['s', 's', 's'])
    def test_jogar_blackjack_explodir(self, mock_shuffle, mock_input):
        sys.stdout = StringIO()

        jogar_blackjack()

        output = sys.stdout.getvalue()
        sys.stdout.close()

        self.assertIn("Você estourou! Você perdeu. Sua pontuação foi", output)
    
    @patch('blackjack.criar_baralho', return_value=['2', '3', 'K', 'A'])
    @patch('builtins.input', return_value='n')
    def test_jogador_faz_21_pontos(self, mock_shuffle, mock_input):
        sys.stdout = StringIO()

        jogar_blackjack()

        output = sys.stdout.getvalue()
        sys.stdout.close()
        self.assertIn("Você tem 21! Você ganhou!", output)

    @patch('blackjack.criar_baralho', return_value=['K', 'A', '2', '3'])
    @patch('builtins.input', return_value='n')
    def test_crupie_faz_21_pontos_jogador_faz_menos(self, mock_shuffle, mock_input):
        sys.stdout = StringIO()

        jogar_blackjack()

        output = sys.stdout.getvalue()
        sys.stdout.close()
        self.assertIn("Você perdeu. Sua pontuação foi", output)

if __name__ == '__main__':
    unittest.main()