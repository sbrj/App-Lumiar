from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


class TelaCachoeiras(Screen):
    '''
    Módulo de apresentacao das cachoeiras
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    lista_janelas = ['pocobelo', 'indiana', 'encontro', 'indiana']
    cachoeiras = ['Poco Belo', 'Indiana', 'Encontro dos Rios', 'Poco Verde']
    fotos = ['lumiar2.jpg','lumiar2.jpg','lumiar2.jpg','lumiar2.jpg']

    def on_pre_enter(self):
        # habilita o método 'voltar'
        Window.bind(on_keyboard=self.voltar)

    def on_enter(self):
        # ao entrar, percorrer a lista de cachoeiras
        for index, cachoeira in enumerate(self.cachoeiras):
            # por cada cachoeira, add widget(módulo(arg1=str,arg2=str,arg3=str))
            self.ids.box.add_widget(GetCachoeira(text=cachoeira,foto=self.fotos[index], desc=self.lista_janelas[index]))
            
    def voltar(self,window,key,*args):
        # se apertar 'esc', retorna menu
        if key == 27: 
            App.get_running_app().root.current = 'menu'
            return True
    
    def on_pre_leave(self):
        # desabilita o método voltar
        Window.unbind(on_keyboard=self.voltar)
        # limpa o módulo TelaCachoeiras antes de sair
        TelaCachoeiras.clear_widgets(self.ids.box)

class GetCachoeira(GridLayout):
    '''
    Módulo que adiciona um gridlayout
    Recebe 3 argumentos:
    :param
        text: Nome da cachoeira
        foto: Nome da foto da cachoeira
        desc: Lista de janelas
    '''
    def __init__(self,text='',foto=str,desc='',**kwargs):
        super().__init__(**kwargs)
        self.cachu = desc
        self.ids.botoes_fotos.background_normal = foto
        self.ids.label.text = text
    
    def get_descricao(self, *args):
        '''
        Função que leva para uma janela
        com a descricao das cachoeiras
        '''
        App.get_running_app().root.current = self.cachu