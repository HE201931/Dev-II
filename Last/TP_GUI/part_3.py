from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class GrilleApp(App):
    
    def __init__(self):
        self.__grille = None

    def build(self):
        self.__grille = GridLayout(cols=5, spacing=5)

        for _ in range(5):
            for _ in range(5):
                case = Button(background_normal='', background_color=(1, 1, 1, 1))
                case.bind(on_press=self.changer_couleur)
                self.__grille.add_widget(case)

        return self.__grille

    def changer_couleur(self, instance):
        couleur_actuelle = instance.background_color
        nouvelle_couleur = [0, 0, 0, 1] if couleur_actuelle == [1, 1, 1, 1] else [1, 1, 1, 1]
        instance.background_color = nouvelle_couleur


if __name__ == '__main__':
    GrilleApp().run()