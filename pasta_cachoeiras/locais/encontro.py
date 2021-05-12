from kivy.uix.screenmanager import Screen

class Encontro(Screen):

    textao = 'Encontro entre Rio Macaé e Rio bonito.  Visual fantástico e natureza belíssima! Tomar cuidado com as crianças pequenas para não escorregarem...' 
    imagem = 'pasta_cachoeiras/pasta_fotos/encontro_rios.jpg'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_enter(self, **kwargs):
        self.ids.imagem_descricao.source = self.imagem
        self.ids.texto_descricao.text = self.textao