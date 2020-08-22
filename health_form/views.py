from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import HealthQuestions
from .forms import HealthQuestionsForm


@login_required
def health_form(request):
    """A view to return the health form"""

    health = HealthQuestions

    if request.method == 'POST':
        form = HealthQuestionsForm(request.POST, instance=health)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your time!')
            return render(request, 'checkout/checkout.html')
        else:
            messages.error(request, 'Form is invalid, please try again')

    form = HealthQuestionsForm()

    context = {

        'form': form,
    }

    return render(request, 'health_form/health_form.html', context)
