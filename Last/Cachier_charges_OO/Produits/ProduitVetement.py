from Produits.BaseProduit import Produit


class ProduitVetement(Produit):
    def __init__(self, id_produit, nom, type_produit, quantite, taille):
        super().__init__(id_produit, nom, type_produit, quantite)
        self.__taille = taille

    def __str__(self):
        return super().__str__() + f"#TAILLE:{self.__taille}"