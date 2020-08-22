from django import forms
from .models import HealthQuestions


class HealthQuestionsForm(forms.ModelForm):
    class Meta:
        model = HealthQuestions
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {

            'how_often': 'How often do you train a week?',
            'what_times': 'What times do you usually train?',
            'favourite_way': 'TWhat is your favourite way to workout?',
            'supplement':
            'Do you supplement your training with any form of diet?',
            'where_you_hear': 'Where did you hear about us?',
        }

        self.fields['how_often'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
