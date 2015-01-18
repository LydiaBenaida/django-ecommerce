# coding=utf-8
from commerce.models import *
from commerce.forms import RegisterForm, AddAddress
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import stripe


def index(request):
    msg = messages.get_messages(request)
    products = Product.objects.select_related('vat').order_by('-id')[:5]
    categories = Category.objects.filter(parent_category_id=None)
    carousel = Photo.objects.all().order_by('-id')[:5]
    # request.session.clear()

    return render(request, 'index.html',
                  {'products': products, 'categories': categories, 'carousel': carousel})


def sign_in(request):
    msg = None

    if request.method == 'POST':

        if 'register' in request.POST:
            form = RegisterForm(request.POST)
        else:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    client = Client.objects.filter(user_id=user.id).first()
                    __move_session_cart_to_database_cart(request, client.id)
                    login(request, user)
                    if request.GET['next']:
                        return redirect(request.GET['next'])
                    else:
                        return redirect(reverse('commerce:root'))
                else:
                    msg = "The password is valid, but the account has been disabled!"
            else:
                # the authentication system was unable to verify the username and password
                msg = "The username and password were incorrect."
    else:
        form = RegisterForm()

    return render(request, 'signin.html', {
        'mes': msg,
        'get': request.GET,
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

    product = get_object_or_404(Product, pk=product_id)
    pictures = Photo.objects.filter(product__pk=product.id)

    return render(request, 'product.html', {'product': product, 'pictures': pictures})


def __move_session_cart_to_database_cart(request, client_id):
    """
    Cette fonction permet de copier le panier stocké en session d'un utilisateur non identifé vers la base de données
    juste avant son identification et supprime ensuite le panier stocké en session.
    :param request: l'objet request transmis depuis la fonction parent pour accéder à la session courante
    :param client_id: l'id du client
    :return:
    """
    if 'cart' in request.session:
        for product_id, qty in request.session['cart'].iteritems():
            if CartLine.objects.filter(product_id=product_id, client_id=client_id).exists():
                cart_line = CartLine.objects.get(product_id=product_id, client_id=client_id)
                cart_line.quantity += int(qty)
            else:
                cart_line = CartLine(product_id=product_id, client_id=client_id, quantity=qty)
            cart_line.save()
        del request.session['cart']
    return


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
    else:
        client = Client.objects.get(user_id=request.user.id)
        if CartLine.objects.filter(product_id=product_id, client_id=client.id).exists():
            cart_line = CartLine.objects.filter(product_id=product_id, client_id=client.id);
            cart_line.quantity += qty
        else:
            cart_line = CartLine(product_id=product_id, client_id=client.id, quantity=qty)
        cart_line.save()

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
    if not request.user.is_authenticated() and 'cart' in request.session:
        del request.session['cart']
    else:
        client = Client.objects.get(user_id=request.user.id)
        CartLine.objects.filter(client_id=client.id).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def display_cart(request):
    total = 0
    if (not request.user.is_authenticated()):
        if 'cart' in request.session:
            for id, qty in request.session['cart'].iteritems():
                cart = list()
                cart_line = CartLine(product_id=id, quantity=qty)
                total += cart_line.total()
                list.append(cart, cart_line)
        else:
            cart = None
    else:
        client = Client.objects.get(user_id=request.user.id)
        cart = CartLine.objects.filter(client_id=client.id)
        for cart_line in cart:
            total += cart_line.total()
    return render(request, 'cart.html', {'cart': cart, 'grand_total': total})


@login_required(login_url='/sign-in')
def shipping(request):
    client = Client.objects.get(user_id=request.user.id)
    addresses= Address.objects.filter(client_id=client.id)

    return render(request, 'shipping.html', {'addresses': addresses})


def add_address(request):
    if request.method == 'POST':
        add_address_form = AddAddress(request.POST)

        if add_address_form.is_valid():
            client = Client.objects.get(user_id=request.user.id)
            address = add_address_form.save(commit=False)
            address.client_id = client.id
            address.save()
            if request.GET['next']:
                return redirect(request.GET['next'])
            else:
                redirect('')
    else:
        add_address_form = AddAddress()
    return render(request, 'add_address.html', {'add_address_form': add_address_form})


def checkout(request):
    total = 0
    client = Client.objects.get(user_id=request.user.id)
    cart = CartLine.objects.filter(client_id=client.id)
    for cart_line in cart:
        total += cart_line.total()
    total_cents = int(round(total*100))

    if request.method == 'POST':
        # Set your secret key: remember to change this to your live secret key in production
        # See your keys here https://dashboard.stripe.com/account
        stripe.api_key = "sk_test_1g1mSv8k1NZxmsfDKvIckMZL"

        # Get the credit card details submitted by the form
        token = request.POST['stripeToken']

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
          charge = stripe.Charge.create(
              amount=total_cents, # amount in cents, again
              currency="eur",
              card=token,
              description=request.user.email
          )
        except stripe.CardError, e:
          # The card has been declined
          pass
    return render(request, 'checkout.html', {'cart': cart, 'grand_total': total, 'grand_total_cents':total_cents, 'user_email': request.user.email})