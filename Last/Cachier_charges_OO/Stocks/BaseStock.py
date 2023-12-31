import datetime

class Stock:
    def __init__(self):
        self.__produits = []

    def get_produits(self):
        return self.__produits

    def set_produits(self, produits):
        self.__produits = produits

    def ajouter_produit(self, produit):
        self.__produits.append(produit)

    def supprimer_produit(self, id_produit):
        self.__produits = [produit for produit in self.__produits if produit.id_produit != id_produit]

    def modifier_produit(self, id_produit, nouveau_produit):
        for i, produit in enumerate(self.__produits):
            if produit.id_produit == id_produit:
                self.__produits[i] = nouveau_produit
                break

    def filtrer_produits_par_type(self, type_produit):
        return [produit for produit in self.__produits if produit.type_produit == type_produit]
