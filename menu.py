from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.core.window import Window


class Menu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_pre_enter(self):
        Window.bind(on_request_close=self.confirmacao)


    def confirmacao(self, *args,**kwargs):
        '''
        Método utilizado para confirmar a saída do App
        '''
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)
        popup = self.PopUp(box, botoes)
        box.add_widget(popup[0])
        box.add_widget(popup[1])
        
        popup[2].open()
        return True 
    
    def PopUp(self, box, botoes,*args):
        pop = Popup(title='Deseja sair?', content=box, size_hint=(None,None),size=(300,180))

        sim = Botao(text='Sim', on_release=App.get_running_app().stop)
        nao = Botao(text='Não', on_release=pop.dismiss)

        botoes.add_widget(sim)
        botoes.add_widget(nao)

        atencao = Image(source='atencao.png')
        return atencao, botoes, pop

class Botao(ButtonBehavior, Label):
    '''
    Propriedades do botao da tela menu
    '''
    cor = ListProperty([0.1,0.4,0.5,1])
    cor2 = ListProperty([0.1,0.2,0.3,1])
    def __init__(self, **kwargs):
        super(Botao,self).__init__(**kwargs)
        self.atualizar()    
    
    def on_pos(self,*args):
        self.atualizar()
    
    def on_size(self,*args):
        self.atualizar()

    def on_press(self, *args):
        self.cor,self.cor2 = self.cor2,self.cor
    
    def on_cor(self,*args):
        self.atualizar()
    
    def on_release(self,*args):
        self.cor = self.cor2

    def atualizar(self,*args):  
        self.canvas.before.clear()     
        with self.canvas.before:
            Color(rgba=(self.cor))
            Ellipse(size=(self.height,self.height),
                    pos=self.pos)
            Ellipse(size=(self.height,self.height),
                    pos=(self.x+self.width-self.height,self.y))
            Rectangle(size=(self.width-self.height,self.height),
                        pos=(self.x+self.height/2.0,self.y))