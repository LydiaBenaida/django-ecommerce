# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from commerce.models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    msg = messages.get_messages(request)
    products = Products.objects.all()
    categories = Category.objects.filter(parent_category_id=None)
    #request.session.clear()

    panier_from_session = request.session.get('cart')

    return render_to_response('index.html', {'products': products, 'categories': categories, 'panier': panier_from_session, 'messages': msg})


def add_to_cart(request, product_id, qty):

    """
    Cette fonction permet d'ajouter un produit au panier. Si l'utilisateur n'est pas connecté, le produit est ajouté
    dans un panier virtuel géré grâce au système de sessions ; sinon, il est persisté en BDD.
    :type request:
    :param request:
    :param product_id: Id du produit à ajouter au panier
    :param qty: Nombre d'exemplaire du produit à ajouter au panier
    :return:
    """
    if not request.user.is_authenticated():
        if not request.session.has_key('cart'):
            cart = dict()
        else:
            cart = request.session['cart']

        if cart.has_key(product_id):
            cart[product_id] = int(cart[product_id]) + int(qty)
        else:
            cart[product_id] = qty

        request.session['cart'] = cart
        lien_panier = '<a style="margin-top:-7px" class="pull-right btn btn-default" href="'+reverse('commerce:display_cart')+'"><i class="fa fa-shopping-cart"></i> Voir le panier</a>'
        lien_dismit = '<button data-dismiss="alert" style="margin-top:-7px; margin-right:10px;" class="pull-right btn btn-default"><i class="fa fa-close"></i> Continuer mes achats</button>'
        messages.add_message(request, messages.SUCCESS, 'Le produit a été correctement ajouté à votre panier. '+lien_panier+lien_dismit)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def clear_cart(request):

    """
    Cette fonction permet de vider le panier. Si l'utilisateur n'est pas connecté, la fonction vide le panier virtuel
    stocké en session ; sinon, les objets précédemment persistés en BDD sont supprimés.
    :param request:
    :return:
    """
    if not request.user.is_authenticated():
        if request.session.has_key('cart'):
            del request.session['cart']

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def display_cart(request):

    if not request.user.is_authenticated() and request.session.has_key('cart'):
        products = Products.objects.filter(id__in=request.session['cart'])
        total = 0
        for product in products:
            cart = request.session['cart']
            qty = cart.get(str(product.id))
            product.qty = int(qty)
            product.ht = product.price * product.qty
            product.tva = product.ht * product.vat.percent
            product.ttc = product.ht + product.tva
            total += product.ttc

        return render_to_response('cart.html', {'products': products, 'total': total})

    else:
        return render_to_response('cart.html')