from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class Gerenciador(ScreenManager):
    '''
    Gerenciador de janelas.
    Chama o modulo Gerenciador no arquivo lumiar.kv
    '''
    pass

class Mercados(Screen):
    pass
        

class LumiarApp(App):
    def build(self):
        return Gerenciador()

if __name__ == '__main__':
    LumiarApp().run()