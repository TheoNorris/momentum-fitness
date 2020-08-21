from django import forms
from .models import HealthQuestions


class HealthQuestionsForm(forms.ModelForm):
    class Meta:
        model = HealthQuestions
        fields = fields = '__all__'
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {

            'user': 'user',
            'how_often': 'How often do you train a week',
            'what_times': 'What times do you usually workout?',
            'favourite_way': "What's your favourite way of training?",
            'supplement': 'Do you supplement your training with a diet plan?',
            'Where_you_hear': 'Where did you hear about us?',
        }
        self.fields['how_often'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
        self.fields[field].widget.attrs['placeholder'] = placeholder

