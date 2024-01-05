import unittest
from datetime import date

from Produits.BaseProduit import TypeProduit
from Produits.ProduitAlimentaire import ProduitAlimentaire
from Produits.ProduitBricolage import ProduitBricolage
from Produits.ProduitElectronique import ProduitElectronique
from Produits.ProduitVetement import ProduitVetement
from Stocks.BaseStock import Stock


class TestStock(unittest.TestCase):

    def setUp(self):
        self.__stock = Stock()

        # Création de quelques produits pour les tests
        self.__produit_bricolage = ProduitBricolage(1, "Marteau", TypeProduit.BRICOLAGE, 10, "Bois")
        self.__produit_alimentaire = ProduitAlimentaire(2, "Pain", TypeProduit.ALIMENTAIRE, 20, ["Gluten"],
                                                        date(2024, 12, 31))
        self.__produit_electronique = ProduitElectronique(3, "Téléphone", TypeProduit.ELECTRONIQUE, 5, 2)
        self.__produit_vetement = ProduitVetement(4, "Chemise", TypeProduit.VETEMENT, 15, "L")

    def test_ajouter_produit(self):
        self.__stock.ajouter_produit(self.__produit_bricolage)
        self.assertIn(self.__produit_bricolage, self.__stock.get_produits())

    def test_supprimer_produit(self):
        self.__stock.ajouter_produit(self.__produit_alimentaire)
        self.__stock.supprimer_produit(self.__produit_alimentaire.id_produit)
        self.assertNotIn(self.__produit_alimentaire, self.__stock.get_produits())

    def test_modifier_produit(self):
        self.__stock.ajouter_produit(self.__produit_electronique)
        nouveau_produit = ProduitElectronique(3, "Nouveau Téléphone", TypeProduit.ELECTRONIQUE, 8, 3)
        self.__stock.modifier_produit(self.__produit_electronique.id_produit, nouveau_produit)
        self.assertIn(nouveau_produit, self.__stock.get_produits())

    def test_filtrer_produits_par_type(self):
        self.__stock.ajouter_produit(self.__produit_bricolage)
        self.__stock.ajouter_produit(self.__produit_alimentaire)
        self.__stock.ajouter_produit(self.__produit_electronique)
        self.__stock.ajouter_produit(self.__produit_vetement)

        produits_bricolage = self.__stock.filtrer_produits_par_type(TypeProduit.BRICOLAGE)
        self.assertEqual(len(produits_bricolage), 1)
        self.assertIn(self.__produit_bricolage, produits_bricolage)


if __name__ == '__main__':
    unittest.main()
