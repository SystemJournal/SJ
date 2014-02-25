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

class EmpresaSpec(unittest.TestCase):
	def it_creates_a_empresa_object(self):
		empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
		empresa.uid |should| equal_to("001")
		empresa.cnpj |should| equal_to("928329")
		empresa.diretorresponsavel |should| equal_to("Paulo Tobias")
		empresa.razaosocial |should| equal_to("Superbom")
		empresa.nomefantasia |should| equal_to("SuperBom")
		empresa.telefonesede |should| equal_to("233434")
		empresa.listadeestabelecimento |should| equal_to([])
		
class CriticoSpec(unittest.TestCase):
	def it_creates_a_critico_object(self):
		critico = Critico("001","Matteus Souza", "Critico", "email@fake", [])
		critico.uid |should| equal_to("001")
		critico.nome |should| equal_to("Matteus Souza")
		critico.cargo |should| equal_to("Critico")
		critico.email |should| equal_to("email@fake")
		critico.listaderesenha |should| equal_to([])		
