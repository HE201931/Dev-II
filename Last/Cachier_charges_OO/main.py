import datetime
from Produits.BaseProduit import TypeProduit
from Produits.ProduitAlimentaire import ProduitAlimentaire
from Produits.ProduitBricolage import ProduitBricolage
from Produits.ProduitElectronique import ProduitElectronique
from Produits.ProduitVetement import ProduitVetement
from Stocks.BaseStock import Stock

if __name__ == '__main__':
    produit1 = ProduitElectronique(1, "Téléphone", TypeProduit.ELECTRONIQUE, 50, "2 ans")
    produit2 = ProduitElectronique(2, "Ordinateur portable", TypeProduit.ELECTRONIQUE, 5, "2 ans")
    produit3 = ProduitVetement(3, "Chemise", TypeProduit.VETEMENT, 30, "L")
    produit4 = ProduitAlimentaire(4, "Pomme", TypeProduit.ALIMENTAIRE, 100, ["A", "B"], datetime.date(2023, 1, 10))
    produit5 = ProduitBricolage(5, "Scie circulaire", TypeProduit.BRICOLAGE, 10, ["Acier", "Plastique"])

    stock = Stock()
    stock.ajouter_produit(produit1)
    stock.ajouter_produit(produit2)
    stock.ajouter_produit(produit3)
    stock.ajouter_produit(produit4)
    stock.ajouter_produit(produit5)

    print("Produits dans le stock:")
    for produit in stock.get_produits():
        print(produit)
