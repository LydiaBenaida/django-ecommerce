from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'commerce.views.index', name='root'),
    url(r'^sign-in/(?P<goto>\w+:\w+)/$', 'commerce.views.sign_in', name='sign_in_goto'),
    url(r'^sign-in/$', 'commerce.views.sign_in', name='sign_in'),
    url(r'^sign-out/$', 'commerce.views.sign_out', name='sign_out'),
    url(r'^product/(?P<product_id>\d+)/$', 'commerce.views.display_product', name='display_product'),
    url(r'^category/(?P<category_id>\d+)$', 'commerce.views.display_category', name='display_category'),
    url(r'^add-to-cart/(?P<product_id>\d+)/(?P<qty>\d+)/$', 'commerce.views.add_to_cart', name='add_to_cart'),
    url(r'^clear-cart/$', 'commerce.views.clear_cart', name='clear_cart'),
    url(r'^display-cart/$', 'commerce.views.display_cart', name='display_cart'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)