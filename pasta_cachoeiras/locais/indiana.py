from kivy.uix.screenmanager import Screen

class Indiana(Screen):
    
    textao = 'Se o astronaura do Brasil sair pra lua, nosso céu será azul piscina.'
    imagem = 'pasta_cachoeiras/pasta_fotos/toca_onca.jpg'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_enter(self, **kwargs):
        self.ids.imagem_descricao.source = self.imagem
        self.ids.texto_descricao.text = self.textao