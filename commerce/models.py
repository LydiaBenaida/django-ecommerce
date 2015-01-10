# -*-coding: UTF-8-*-
from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    """
    Un client est une personne inscrite au site dans le but d'effectuer une commande.
    """
    user = models.ForeignKey(User, verbose_name="Utilisateur associé")
    default_shipping_address = models.ForeignKey("Address", related_name="default_shipping_address", null=True, verbose_name="Adresse de livraison par défaut")
    default_invoicing_address = models.ForeignKey("Address", related_name="default_invoicing_address", null=True, verbose_name="Adresse de facturation par défaut")

    def __unicode__(self):
        return self.user.username + " (" + self.user.first_name + " " + self.user.last_name + ")"


class Address(models.Model):
    """
    Une adresse est liée à un client et pourra être utilisée pour la livraison ou la facturation d'une commande.
    """
    client = models.ForeignKey(Client)
    MISTER = 'MR'
    MISS = 'MISS'
    MISSES = 'MRS'
    GENDER = (
        (MISTER, 'Monsieur'),
        (MISS, 'Mademoiselle'),
        (MISSES, 'Madame'),
    )
    gender = models.CharField(max_length=4, choices=GENDER, default=MISTER, verbose_name="Civilité")
    first_name = models.CharField(max_length=50, verbose_name="Prénom")
    last_name = models.CharField(max_length=50, verbose_name="Nom")
    company = models.CharField(max_length=50, blank=True, verbose_name="Société")
    address = models.CharField(max_length=255, verbose_name="Adresse")
    additional_address = models.CharField(max_length=255, blank=True, verbose_name="Complément d'adresse")
    country = models.CharField(max_length=150, verbose_name="Pays")
    postcode = models.CharField(max_length=5, verbose_name="Code postal")
    city = models.CharField(max_length=50, verbose_name="Ville")
    phone = models.CharField(max_length=10, verbose_name="Téléphone")
    mobilephone = models.CharField(max_length=10, blank=True, verbose_name="Téléphone portable")
    fax = models.CharField(max_length=10, blank=True, verbose_name="Fax")
    workphone = models.CharField(max_length=10, blank=True, verbose_name="Téléphone travail")

    class Meta:
        verbose_name ='Adresse'
        verbose_name_plural = 'Adresses'

    def __unicode__(self):
        return self.address


class VAT(models.Model):
    """
    Les différents taux de TVA sont associés à des produits.
    """
    percent = models.FloatField(verbose_name="Taux de TVA (décimal)")

    class Meta:
        verbose_name ='Taux de TVA'
        verbose_name_plural = 'Taux de TVA'

    def __unicode__(self):
        return str(self.percent * 100) + " %"


class Category(models.Model):
    """
    Les catégories permettent d'organiser les produits en rayons d'articles similaires.
    """
    name = models.CharField(max_length=150, verbose_name="Nom de la catégorie")
    short_desc = models.CharField(max_length=150, verbose_name="Description courte",blank=True)
    parent_category = models.ForeignKey("Category", null=True, blank=True, verbose_name="Catégorie parente")

    class Meta:
        verbose_name ='Catégorie de produits'
        verbose_name_plural = 'Catégories de produits'

    def __unicode__(self):
        return self.name


class Products(models.Model):
    """
    Les produits sont rangés par catégories et sont référencés dans des lignes de commandes.
    """
    name = models.CharField(max_length=150, verbose_name="Nom du produit")
    category = models.ForeignKey(Category, verbose_name="Catégorie du produit")
    short_desc = models.CharField(max_length=150, verbose_name="Description courte")
    long_desc = models.TextField(verbose_name="Description longue")
    price = models.FloatField(verbose_name="Prix HT du produit")
    vat = models.ForeignKey(VAT, verbose_name="Taux de TVA")

    class Meta:
        verbose_name ='Produit'
        verbose_name_plural = 'Produits'

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    """
    Les photos permettent d'illustrer les produits afin d'inciter l'internaute à les acheter.
    """
    produit = models.ForeignKey(Products)
    photo = models.ImageField()


class Order(models.Model):
    """
    Une commande est passée par un client et comprend des lignes de commandes ainsi que des adresses.
    """
    client = models.ForeignKey(Client, verbose_name="Client ayant passé commande")
    shipping_address = models.ForeignKey(Address, verbose_name="Adresse de livraison", related_name="order_shipping_address")
    invoicing_address = models.ForeignKey(Address, verbose_name="Adresse de facturation", related_name="order_invoicing_address")
    order_date = models.DateField(verbose_name="Date de la commande",auto_now=True)
    shipping_date = models.DateField(verbose_name="Date de l'expédition",blank=True)
    WAITING = 'W'
    PAID = 'P'
    SHIPPED = 'S'
    CANCELED = 'C'
    STATUS = (
        (WAITING, 'En attente de validation'),
        (PAID, 'Payée'),
        (SHIPPED, 'Expédiée'),
        (CANCELED, 'Annulée'),
    )
    status = models.CharField(max_length=1, choices=STATUS, default=WAITING, verbose_name="Statut de la commande")
    price = models.FloatField(verbose_name="Montant total")

    class Meta:
        verbose_name ='Commande'
        verbose_name_plural = 'Commandes'


class OrderDetail(models.Model):
    """
    Une ligne de commande référence un produit, la quantité commandée ainsi que les prix associés.
    Elle est liée à une commande.
    """
    order = models.ForeignKey(Order, verbose_name="Commande associée")
    product = models.ForeignKey(Products)
    qty = models.IntegerField(verbose_name="Quantité")
    price = models.FloatField(verbose_name="Prix HT")
    vat = models.FloatField(verbose_name="TVA")
    total_price = models.FloatField(verbose_name="Prix TTC")

    class Meta:
        verbose_name ='Ligne d\'une commande'
        verbose_name_plural = 'Lignes de commandes'