from Produits.BaseProduit import Produit


class ProduitBricolage(Produit):
    def __init__(self, id_produit, nom, type_produit, quantite, materiaux):
        super().__init__(id_produit, nom, type_produit, quantite)
        self.__materiaux = materiaux

    def __str__(self):
        return super().__str__() + f"#MATERIAUX:{self.__materiaux}"
