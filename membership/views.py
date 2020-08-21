from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Article, HealthQuestions
from .forms import HealthQuestionsForm


def membership(request):
    """A view to return the membership page"""
    products = Product.objects.filter(category__name='Membership')

    context = {
        'products': products,
    }

    return render(request, 'membership/membership.html',  context)


@login_required
def health_form(request):
    """A view to return the health form"""

    health = get_object_or_404(HealthQuestions, user=request.user)

    if request.method == 'POST':
        form = HealthQuestionsForm(request.POST, instance=health)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your time!')
            return render(request, 'checkout/checkout.html')
        else:
            messages.error(request, 'Form is invalid, please try again')

    form = HealthQuestionsForm(instance=health)

    template = 'membership/health_form.html'

    context = {

        'form': form,
    }

    return render(request, template, context)


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

    """A view to return the members only page"""
    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article': article,
    }

    return render(request, 'membership/members_articles.html', context)
