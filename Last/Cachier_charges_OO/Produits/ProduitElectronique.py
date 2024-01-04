from Produits.BaseProduit import Produit


class ProduitElectronique(Produit):
    def __init__(self, id_produit, nom, type_produit, quantite, garantie):
        super().__init__(id_produit, nom, type_produit, quantite)
        self.__garantie = garantie

    def __str__(self):
        return super().__str__() + f"#GARANTIE:{self.__garantie}"
