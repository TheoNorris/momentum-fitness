from django.shortcuts import get_object_or_404
from django.shortcuts import render
from products.models import Product
from .models import Article


def membership(request):
    products = Product.objects.filter(category__name='Membership')

    context = {
        'products': products,
    }
    """A view to return the membership page"""
    return render(request, 'membership/membership.html',  context)


def members_only(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    """A view to return the members only page"""
    return render(request, 'membership/members_only.html', context)


def members_articles(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
    }

    """A view to return the members only page"""
    return render(request, 'membership/members_articles.html', context)
