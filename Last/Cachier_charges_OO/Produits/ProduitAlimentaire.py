from Produits.BaseProduit import Produit


class ProduitAlimentaire(Produit):
    def __init__(self, id_produit, nom, type_produit, quantite, allergenes, date_peremption):
        super().__init__(id_produit, nom, type_produit, quantite)
        self.allergenes = allergenes
        self.__date_peremption = date_peremption

    def __str__(self):
        return super().__str__() + f"#DATE_PEREMPTION:{self.__date_peremption}"
