from kivy.uix.screenmanager import Screen

class PocoBelo(Screen):
    
    textao = "Um belo local, de fácil acesso, com uma pequena queda d'água e um lindo poço para se refrescar, inclusive com crianças, além claro, de ser um belo local para tirar fotos."
    imagem = 'pasta_cachoeiras/pasta_fotos/poco-belo.jpg'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_enter(self, **kwargs):
        self.ids.imagem_descricao.source = self.imagem
        self.ids.texto_descricao.text = self.textao