# coding=utf-8
from commerce.models import *
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='Votre prénom', required=True)
    last_name = forms.CharField(label='Votre nom', required=True)
    username = forms.CharField(label='Votre nom d\'utilisateur', required=True)
    password = forms.CharField(label='Votre mot de passe',required=True, widget=forms.PasswordInput)
    email = forms.EmailField(label='Votre adresse e-mail', required=True)


def index(request):
    msg = messages.get_messages(request)
    products = Products.objects.select_related('vat').order_by('-id')[:5]
    categories = Category.objects.filter(parent_category_id=None)
    carousel = Photo.objects.all().order_by('-id')[:5]
    # request.session.clear()

    return render(request, 'index.html',
                  {'products': products, 'categories': categories, 'carousel': carousel})


def sign_in(request, goto='commerce:root'):
    msg = None
    form = RegisterForm()
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse(goto))
            else:
                msg = "The password is valid, but the account has been disabled!"
        else:
            # the authentication system was unable to verify the username and password
            msg = "The username and password were incorrect."

    return render(request, 'signin.html', {
        'mes': msg,
        'goto': goto,
        'form': form
    })


def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('commerce:root'))


def display_category(request, category_id):
    """
    Cette fonction permet de visualiser les produits contenus dans une catégorie.
    :type request:
    :param request:
    :param category_id: Id de la catégorie à visualiser
    :return:
    """
    category = get_object_or_404(Category, pk=category_id)
    product_list = category.all_products()
    paginator = Paginator(product_list, 12)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category': category, 'products': products})


def display_product(request, product_id):
    """
    Cette fonction permet de visualiser un produit.
    :type request:
    :param request:
    :param product_id: Id du produit à visualiser
    :return:
    """

    product = get_object_or_404(Products, pk=product_id)
    pictures = Photo.objects.filter(product__pk=product.id)

    return render(request, 'product.html', {'product': product, 'pictures': pictures})


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
        if 'cart' not in request.session:
            cart = dict()
        else:
            cart = request.session['cart']

        if product_id in cart:
            cart[product_id] = int(cart[product_id]) + int(qty)
        else:
            cart[product_id] = qty

        request.session['cart'] = cart
        lien_panier = '<a style="margin-top:-7px" class="pull-right btn btn-default" href="' + reverse(
            'commerce:display_cart') + '"><i class="fa fa-shopping-cart"></i> Voir le panier</a>'
        lien_dismit = '<button data-dismiss="alert" style="margin-top:-7px; margin-right:10px;" ' +\
                      'class="pull-right btn btn-default"><i class="fa fa-close"></i> Continuer mes achats</button>'
        messages.add_message(request, messages.SUCCESS,
                             'Le produit a été correctement ajouté à votre panier. ' + lien_panier + lien_dismit
                             )

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def clear_cart(request):
    """
    Cette fonction permet de vider le panier. Si l'utilisateur n'est pas connecté, la fonction vide le panier virtuel
    stocké en session ; sinon, les objets précédemment persistés en BDD sont supprimés.
    :param request:
    :return:
    """
    if not request.user.is_authenticated():
        if 'cart' in request.session:
            del request.session['cart']

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def display_cart(request):
    if not request.user.is_authenticated() and 'cart' in request.session:
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

        return render(request, 'cart.html', {'products': products, 'total': total})

    else:
        return render(request, 'cart.html')