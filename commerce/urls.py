from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'commerce.views.index', name='root'),
    url(r'^add-to-cart/(?P<product_id>\d+)/(?P<qty>\d+)/$', 'commerce.views.add_to_cart', name='add_to_cart'),
    url(r'^clear-cart/$', 'commerce.views.clear_cart', name='clear_cart'),
    url(r'^display-cart/$', 'commerce.views.display_cart', name='display_cart'),
)