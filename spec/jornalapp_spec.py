#coding: utf-8
import unittest
from should_dsl import should
from jornalapp import *


class UsuarioSpec(unittest.TestCase):
    def it_creates_a_usuario_object(self):
        usuario = Usuario("001","Marcos Menna","122323","marcoemailfake@emai.com",[])
        usuario.uid |should| equal_to("001")
        usuario.nome |should| equal_to("Marcos Menna")
        usuario.cpf |should| equal_to("122323")
        usuario.email |should| equal_to("marcoemailfake@emai.com")
        usuario.listaDeAvaliacao |should| equal_to([])
