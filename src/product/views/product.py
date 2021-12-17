from django.views import generic
from django.views.generic import ListView, TemplateView
from product.models import Product, Variant, ProductVariant, ProductVariantPrice


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductListView(TemplateView):
    template_name = 'products/list.html'
    # model = Product
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_variant_price'] = ProductVariantPrice.objects.all()

        return context

