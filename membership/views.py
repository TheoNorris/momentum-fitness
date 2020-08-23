from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Article


def membership(request):
    """A view to return the membership purchase page"""
    products = Product.objects.filter(category__name='Membership')

    context = {
        'products': products,
    }

    return render(request, 'membership/membership.html',  context)


@login_required
def members_only(request):
    """A view to return the members only page"""
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'membership/members_only.html', context)


@login_required
def members_articles(request, article_id):

    """A view to return a members only page"""
    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
    }

    return render(request, 'membership/members_articles.html', context)
