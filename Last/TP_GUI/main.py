from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup


class CalculateurApp(App):
    def build(self):
        self.__layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.__layout_operations = BoxLayout(orientation='horizontal', spacing=5)

        self.__checkbox_addition = CheckBox(group='operation', active=True)
        self.__checkbox_soustraction = CheckBox(group='operation')
        self.__checkbox_multiplication = CheckBox(group='operation')
        self.__checkbox_division = CheckBox(group='operation')

        self.__layout_operations.add_widget(self.__checkbox_addition)
        self.__layout_operations.add_widget(Label(text="Addition"))
        self.__layout_operations.add_widget(self.__checkbox_soustraction)
        self.__layout_operations.add_widget(Label(text="Soustraction"))
        self.__layout_operations.add_widget(self.__checkbox_multiplication)
        self.__layout_operations.add_widget(Label(text="Multiplication"))
        self.__layout_operations.add_widget(self.__checkbox_division)
        self.__layout_operations.add_widget(Label(text="Division"))

        self.__zone_texte1 = TextInput(multiline=False, input_type='number')
        self.__zone_texte2 = TextInput(multiline=False, input_type='number')

        self.__bouton_calculer = Button(text="Calculer")
        self.__bouton_calculer.bind(on_press=self.calculer)

        self.__label_resultat = Label(text="Résultat :")

        self.__layout.add_widget(self.__zone_texte1)
        self.__layout.add_widget(self.__zone_texte2)
        self.__layout.add_widget(Label(text="Opération :"))
        self.__layout.add_widget(self.__layout_operations)
        self.__layout.add_widget(self.__bouton_calculer)
        self.__layout.add_widget(self.__label_resultat)

        return self.__layout

    def calculer(self, instance):
        try:
            nombre_1 = float(self.__zone_texte1.text)
            nombre_2 = float(self.__zone_texte2.text)
            operation = self.obtenir_operation()

            if operation == 1:
                resultat = nombre_1 + nombre_2
            elif operation == 2:
                resultat = nombre_1 - nombre_2
            elif operation == 3:
                resultat = nombre_1 * nombre_2
            elif operation == 4:
                if nombre_2 != 0:
                    resultat = nombre_1 / nombre_2
                else:
                    self.afficher_erreur("Division par zéro.")
                    return

            self.__label_resultat.text = f"Résultat : {resultat:.2f}"

        except ValueError:
            self.afficher_erreur("Veuillez entrer des nombres valides.")

    def obtenir_operation(self):
        if self.__checkbox_addition.active:
            return 1
        elif self.__checkbox_soustraction.active:
            return 2
        elif self.__checkbox_multiplication.active:
            return 3
        elif self.__checkbox_division.active:
            return 4

    def afficher_erreur(self, message):
        popup = Popup(title='Erreur', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()


if __name__ == '__main__':
    CalculateurApp().run()
