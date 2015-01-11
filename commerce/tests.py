# -*- coding: UTF-8 -*-
import os
import sys
import time
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings

from commerce.models import *

class CommerceTest(TestCase):

    def setUp(self):
        self.jean = User.objects.create_user('jean','jean@test.com','jean')
        self.fo_client = Client.objects.create(user=self.jean)

        self.cat1 = Category.objects.create(name='Jeux vidéos',
                                            short_desc='Des jeux vidéos pour vous amuser et vous divertir')
        self.cat11 = Category.objects.create(name='Jeux vidéos Windows',
                                            short_desc='Des jeux vidéos pour vous amuser et vous divertir sous Windows',
                                            parent_category=self.cat1)
        self.cat12 = Category.objects.create(name='Jeux vidéos OS X',
                                            short_desc='Des jeux vidéos pour vous amuser et vous divertir sous Windows',
                                            parent_category=self.cat1)
        self.cat13 = Category.objects.create(name='Jeux vidéos Multiplatesformes',
                                            short_desc='Des jeux vidéos pour vous amuser et vous divertir sur vos différents OS',
                                            parent_category=self.cat1)
        self.cat2 = Category.objects.create(name='Logiciels & Applications',
                                            short_desc='Des outils pour travailler et booster votre productivité')
        self.cat21 = Category.objects.create(name='Environnements de développement',
                                            short_desc='Envie de créer vos propres applications ?',
                                            parent_category=self.cat2)
        self.cat211 = Category.objects.create(name='Environnements de développement Windows',
                                            short_desc='Développez vos propres applications et propulsez-les sur Windows',
                                            parent_category=self.cat21)
        self.cat211 = Category.objects.create(name='Environnements de développement OS X',
                                            short_desc='Développez vos propres applications et propulsez-les sur OS X',
                                            parent_category=self.cat21)
        self.cat211 = Category.objects.create(name='Environnements de développement Muliplateformes',
                                            short_desc='éveloppez vos propres applications et propulsez-les !D',
                                            parent_category=self.cat21)

        self.vat20 = VAT.objects.create(percent='0.20')

        self.product1 = Products.objects.create(name='Pinball',
                                                category=self.cat11,
                                                short_desc='Un jeu de flipper vraiment amusant',
                                                long_desc='Microsoft Pinball 3D : Cadet de l\'espace est un jeu vidéo de flipper fourni avec divers produits Microsoft. Il a été à l\'origine fourni avec Microsoft Plus! 95 et plus tard inclus dans Windows NT, Windows Me, Windows 2000 et Windows XP.',
                                                price='0.0',
                                                vat=self.vat20)
        self.product2 = Products.objects.create(name='Age Of Empire I',
                                                category=self.cat11,
                                                short_desc='Le premier jeu vidéo de stratégie de Microsoft',
                                                long_desc='Age of Empires (souvent abrégé en AoE) est un jeu vidéo de stratégie en temps réel développé par Ensemble Studios et publié par Microsoft Game Studios le 15 octobre 1997 en Amérique du Nord et le 2 février 1998 en Europe et au Japon. L\'action du jeu se déroule dans un contexte historique, sur une période comprise entre 5000 av. J.-C. et 800 ap. J.-C. au cours de laquelle le joueur doit faire évoluer une civilisation antique de l’âge de la pierre à l’âge du fer pour débloquer de nouvelles technologies et unités lui permettant de bâtir un empire. Douze civilisations sont disponibles dans le jeu, chacune d\'elle s\'inspirant de périodes historiques telles que l’Égypte antique et la Grèce antique ou la Mésopotamie. À sa sortie, son contexte historique lui permet de se démarquer des autres jeux de stratégie en temps réel, ce qui lui vaut d\'être bien accueilli par la presse spécialisée. Il connaît rapidement un important succès commercial qui lui permet de se vendre à plus de trois millions d\'exemplaires et de contribuer à faire de Microsoft Game Studios un acteur majeur du secteur du jeu vidéo.',
                                                price='5.20',
                                                vat=self.vat20)
        self.product3 = Products.objects.create(name='Age Of Empire II',
                                                category=self.cat11,
                                                short_desc='Une évolution du premier volet de Microsoft avec de nombreuses améliorations',
                                                long_desc='Age of Empires II : The Age of Kings (souvent abrégé en AoK) est un jeu vidéo de stratégie en temps réel développé par Ensemble Studios et publié sur PC et MAC par Microsoft en 1999. Le jeu est le deuxième épisode de la série après Age of Empires, publié en 1997, et utilise le même moteur de jeu basé sur des sprites en 2D isométrique. L\'action du jeu se déroule dans un contexte historique pendant le Moyen Âge, le joueur devant faire évoluer une civilisation à travers quatre âge - l’âge sombre, l’âge féodal, l’âge des châteaux et l’âge impérial - pour débloquer de nouvelles technologies et unités lui permettant de bâtir un empire. Treize civilisations sont disponibles dans le jeu, chacune d\'elle s\'inspirant de civilisations moyenâgeuses d\'Europe de l’Ouest, d\'Europe de l’Est, du Moyen-Orient et de l\'Asie de l’Est. Comme son prédécesseur, le jeu est bien accueilli par la presse spécialisée et le public grâce notamment à son contexte historique et aux améliorations apportées au système de jeu du premier opus de la série. Plus de deux millions de copies du jeu sont ainsi mises en ventes trois mois après sa sortie et il se classe quatrième des meilleurs ventes de jeux vidéo en 1999.',
                                                price='7.30',
                                                vat=self.vat20)
        self.product4 = Products.objects.create(name='Age Of Empire III',
                                                category=self.cat11,
                                                short_desc='On atteind l\'époque coloniale',
                                                long_desc='Age of Empires III est un jeu vidéo de stratégie en temps réel développé par Ensemble Studios et publié par Microsoft Game Studios le 18 octobre 2005 en Amérique du Nord et le 4 novembre 2005 en Europe. Il est le troisième volet de la série Age of Empires qui fait suite à Age of Empires II: The Age of Kings publié en 1999. Le jeu se déroule pendant l\'époque coloniale, entre 1492 et 1850, dans le nouveau monde. Le joueur y incarne le leader d\'une des huit civilisations disponibles dans le jeu - les Français, les Espagnols, les Portugais, les Hollandais, les Allemands, les Russes, les Ottomans et les Britanniques - qu\'il doit faire évoluer à travers cinq âge pour débloquer de nouvelles technologies et unités. Le jeu reprend les principaux éléments de gameplay de ses prédecesseurs qu\'il transpose dans un univers en trois dimensions basé sur le moteur graphique d\'Age of Mythology.',
                                                price='9.80',
                                                vat=self.vat20)
        self.product5 = Products.objects.create(name='Age Of Mythology',
                                                category=self.cat11,
                                                short_desc='Vivez la mythologie et les légendes de la Grèce, de l\'Egypte et des pays nordiques !',
                                                long_desc='Age of Mythology (souvent abrégé en AoM) est un jeu vidéo de stratégie en temps réel développé par Ensemble Studios et publié par Microsoft Game Studios le 30 octobre 2002 en Amérique du Nord et en novembre 2002 en Europe. Le jeu est un spin-off de la série Age of Empires dont il reprend de nombreux éléments de gameplay en les transposant dans un univers inspiré de la mythologie et des légendes de la Grèce, de l’Égypte et des pays nordiques plutôt que de la réalité historique. La campagne de Age of Mythology suit un amiral Atlante pourchassant un cyclope, s’étant allié à Poséidon pour combattre le royaume de l’Atlantide, à travers les terres des trois civilisations du jeu. Il se démarque de ses prédécesseurs par une plus forte différenciation entre les civilisations ainsi qu\'en introduisant de nouveaux types d\'unités, comme les héros et les créatures mythiques, et un système de divinités permettant de débloquer des pouvoirs divins et des technologies.',
                                                price='12.38',
                                                vat=self.vat20)

    def test_homepage_not_authenticated_user(self):
        time.sleep(10)
        url = reverse('commerce:dashboard')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'commerce/index.html')
        self.failUnlessEqual(response.status_code, 200)