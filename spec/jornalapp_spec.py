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

    def it__consumo_media_test(self):
        empresa1 = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimento1 = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa1, [], [])
        estabelecimento2 = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa1, [], [])
        usuarioTest = Usuario("001","Marcos Menna","122323","marcoemailfake@emai.com",[])
        avaliacaoTu = Avaliacao("001","Pao com Alho",5, 15.0, usuarioTest, estabelecimento1)
        avaliacaoTd = Avaliacao("002","Pao com Manteiga",1, 25.0, usuarioTest, estabelecimento2)
        usuarioTest.inserirAvaliacao(avaliacaoTu)
        usuarioTest.inserirAvaliacao(avaliacaoTd)
        usuarioTest.verificarMediaDeConsumo() |should| equal_to(20.0)

    
    def it_inserir_lista_object(self):
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimento = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        usuario = Usuario("001","Marcos Menna","122323","marcoemailfake@emai.com",[])
        avaliacao = Avaliacao("001","Pao com Alho",5,233, usuario, estabelecimento)
        usuario.inserirAvaliacao(avaliacao)
        (avaliacao in usuario.listaDeAvaliacao) |should| equal_to(True)
    
    def it_verificar_lista_object(self):
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimento = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        usuario = Usuario("001","Marcos Menna","122323","marcoemailfake@emai.com",[])
        avaliacao = Avaliacao("001","Pao com Alho",5,233, usuario, estabelecimento)
        usuario.inserirAvaliacao(avaliacao)
        usuario.verificarAvaliacao(avaliacao) |should| equal_to(True)

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

    def it_inserir_lista_estabelecimento_(self):
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimento = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        empresa.inserirEstabelecimento(estabelecimento)
        (estabelecimento in empresa.listadeestabelecimento) |should| equal_to(True)

    def it_verificar_lista_estabelecimento_(self):
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimento = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        empresa.inserirEstabelecimento(estabelecimento)
        empresa.verificarEstabelecimento(estabelecimento) |should| equal_to(True)

    def it_verificar_media_empresa(self):
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimentoUm = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        usuario = Usuario("001","Marcos Menna","122323","marcoemailfake@emai.com",[])
        avaliacaoUm = Avaliacao("001","Pao com Alho",5,233, usuario, estabelecimentoUm)
        avaliacaoDois = Avaliacao("002","Pao com Manteiga",1,233, usuario, estabelecimentoUm)
        estabelecimentoUm.inserirAvaliacao(avaliacaoUm)
        estabelecimentoUm.inserirAvaliacao(avaliacaoDois)
        estabelecimentoDois = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        avaliacaoTres = Avaliacao("001","Pao com Queito",2,233, usuario, estabelecimentoDois)
        avaliacaoQuatro = Avaliacao("002","Pao com Cebola",4,233, usuario, estabelecimentoDois)
        estabelecimentoDois.inserirAvaliacao(avaliacaoTres)
        estabelecimentoDois.inserirAvaliacao(avaliacaoQuatro) 
        empresa.inserirEstabelecimento(estabelecimentoUm)
        empresa.inserirEstabelecimento(estabelecimentoDois)
        empresa.mediaDaEmpresa() |should| equal_to(3)

    def it_verificar_estabelecimento_acima_media(self):
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimentoUm = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        usuario = Usuario("001","Marcos Menna","122323","marcoemailfake@emai.com",[])
        avaliacaoUm = Avaliacao("001","Pao com Alho",5,233, usuario, estabelecimentoUm)
        avaliacaoDois = Avaliacao("002","Pao com Manteiga",8,233, usuario, estabelecimentoUm)
        estabelecimentoUm.inserirAvaliacao(avaliacaoUm)
        estabelecimentoUm.inserirAvaliacao(avaliacaoDois)
        estabelecimentoDois = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        avaliacaoTres = Avaliacao("001","Pao com Queito",2,233, usuario, estabelecimentoDois)
        avaliacaoQuatro = Avaliacao("002","Pao com Cebola",4,233, usuario, estabelecimentoDois)
        estabelecimentoDois.inserirAvaliacao(avaliacaoTres)
        estabelecimentoDois.inserirAvaliacao(avaliacaoQuatro) 
        empresa.inserirEstabelecimento(estabelecimentoUm)
        empresa.inserirEstabelecimento(estabelecimentoDois)
        lista = []
        lista.append(estabelecimentoUm)
        empresa.estabelecimentoAcimadaMedia() |should| equal_to(lista)

		
class CriticoSpec(unittest.TestCase):
    def it_creates_a_critico_object(self):
        critico = Critico("001","Matteus Souza", "Critico", "email@fake", [])
        critico.uid |should| equal_to("001")
        critico.nome |should| equal_to("Matteus Souza")
        critico.cargo |should| equal_to("Critico")
        critico.email |should| equal_to("email@fake")
        critico.listaderesenha |should| equal_to([])

    def it_inserir_lista_resenha_(self):
        critico = Critico("001","Matteus Souza", "Critico", "email@fake", [])
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimento = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        resenha = Resenha("001", "Escrevendo um texto aqui", critico, estabelecimento)
        critico.inserirResenha(resenha)
        (resenha in critico.listaderesenha) |should| equal_to(True)

    def it_verificar_lista_resenha(self):
        critico = Critico("001","Matteus Souza", "Critico", "email@fake", [])
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimento = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        resenha = Resenha("001", "Escrevendo um texto aqui", critico, estabelecimento)
        critico.inserirResenha(resenha)
        critico.verificarResenha(resenha) |should| equal_to(True)

    def it_verificar_total_de_resenhas(self):
        critico = Critico("001","Matteus Souza", "Critico", "email@fake", [])
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimentoUm = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        estabelecimentoDois = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        resenhaUm = Resenha("001", "Escrevendo um texto aqui",critico,estabelecimentoUm)
        resenhaDois = Resenha("001", "Escrevendo um texto aqui",critico,estabelecimentoDois)
        critico.inserirResenha(resenhaUm)
        critico.inserirResenha(resenhaDois)
        critico.totalResenhas() |should| equal_to(2)

    
class EstabelecimentoSpec(unittest.TestCase):
    def it_creates_a_estabelecimento_object(self):
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimento = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        estabelecimento.uid |should| equal_to("001")
        estabelecimento.endereco |should| equal_to("Centro")
        estabelecimento.gerenteresponsavel |should| equal_to("Jaum")
        estabelecimento.ramo |should| equal_to("FastFood")
        estabelecimento.telefone |should| equal_to("232312")
        estabelecimento.empresa |should| equal_to(empresa)
        estabelecimento.listaDeAvaliacao |should| equal_to([])
        estabelecimento.listaderesenha |should| equal_to([])

    def it_inserir_lista_resenha(self):
        critico = Critico("001","Matteus Souza", "Critico", "email@fake", [])
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimento = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        resenha = Resenha("001", "Escrevendo um texto aqui", critico, estabelecimento)
        estabelecimento.inserirResenha(resenha)
        (resenha in estabelecimento.listaderesenha) |should| equal_to(True)
    def it_verificar_lista_resenha(self):
        critico = Critico("001","Matteus Souza", "Critico", "email@fake", [])
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimento = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        resenha = Resenha("001", "Escrevendo um texto aqui", critico, estabelecimento)
        estabelecimento.inserirResenha(resenha)
        estabelecimento.verificarResenha(resenha) |should| equal_to(True)

    def it_inserir_lista_avaliacao(self):
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimento = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        usuario = Usuario("001","Marcos Menna","122323","marcoemailfake@emai.com",[])
        avaliacao = Avaliacao("001","Pao com Alho",5,233, usuario, estabelecimento)
        estabelecimento.inserirAvaliacao(avaliacao)
        (avaliacao in estabelecimento.listaDeAvaliacao) |should| equal_to(True)
    def it_verificar_lista_avaliacao(self):
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimento = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        usuario = Usuario("001","Marcos Menna","122323","marcoemailfake@emai.com",[])
        avaliacao = Avaliacao("001","Pao com Alho",5,233, usuario, estabelecimento)
        estabelecimento.inserirAvaliacao(avaliacao)
        estabelecimento.verificarAvaliacao(avaliacao) |should| equal_to(True)

    def it_verificar_media_do_estabelecimento(self):
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimento = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        usuario = Usuario("001","Marcos Menna","122323","marcoemailfake@emai.com",[])
        avaliacaoUm = Avaliacao("001","Pao com Alho",4,233, usuario, estabelecimento)
        avaliacaoDois = Avaliacao("002","Pao com Manteiga",4,233, usuario, estabelecimento)
        estabelecimento.inserirAvaliacao(avaliacaoUm)
        estabelecimento.inserirAvaliacao(avaliacaoDois)
        estabelecimento.mediaDeNova() |should| equal_to(4)


class AvaliacaoSpec(unittest.TestCase):
    def it_creates_a_avaliacao_object(self):
        empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
        estabelecimento = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
        usuario = Usuario("001","Marcos Menna","122323","marcoemailfake@emai.com",[])
        avaliacao = Avaliacao("001","Pao com Alho",5,233, usuario, estabelecimento)
        avaliacao.uid |should| equal_to("001")
        avaliacao.alimentosConsumidos |should| equal_to("Pao com Alho")
        avaliacao.nota |should| equal_to(5)
        avaliacao.precoTotal |should| equal_to(233)
        avaliacao.usuario |should| equal_to(usuario)
        avaliacao.estabelecimento |should| equal_to(estabelecimento)
        
class ResenhaSpec(unittest.TestCase):
	def it_creates_a_resenha_object(self):
		critico = Critico("001","Matteus Souza", "Critico", "email@fake", [])
		empresa = Empresa("001", "928329", "Paulo Tobias", "Superbom", "SuperBom", "233434", [])
		estabelecimento = Estabelecimento("001", "Centro", "Jaum", "FastFood", "232312", empresa, [], [])
		resenha = Resenha("001", "Escrevendo um texto aqui", critico, estabelecimento)
		resenha.uid |should| equal_to("001")
		resenha.resenha |should| equal_to("Escrevendo um texto aqui")
		resenha.critico|should| equal_to(critico)
		resenha.estabelecimento |should| equal_to(estabelecimento)
