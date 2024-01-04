from enum import Enum


class TypeProduit(Enum):
    ALIMENTAIRE = 0
    BRICOLAGE = 1
    ELECTRONIQUE = 2
    VETEMENT = 3


class Produit:
    def __init__(self, id_produit, nom, type_produit, quantite):  # date_peremption):
        self.__id_produit = id_produit
        self.__nom = nom
        self.__type_produit = TypeProduit(type_produit)
        self.__quantite = quantite
        # self.__date_peremption = datetime.datetime.strptime(date_peremption, "%Y-%m-%d").date()

    def __str__(self):
        return f"#ID:{self.__id_produit}#NOM:{self.__nom}#TYPE:{self.__type_produit}#QUANTITE:{self.__quantite}"
