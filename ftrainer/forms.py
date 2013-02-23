from django import forms
from django.utils.translation import ugettext_lazy as _

from ftrainer.models import Exercise

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div


class ExerciseForm(forms.ModelForm):

    class Meta:
        model = Exercise
        exclude = ('user', 'position', 'date', 'date_mod', 'enable_comments',)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('publish', _('Publish')))
        self.helper.add_input(Submit('draft', _('Save to draft')))
        self.helper.layout = Layout(
            Div(
                #'Content',
                'title',
                'part',
                'skill',
                'content',
                'video',
                'structure',
                'complexity',
            ),
        )
        super(ExerciseForm, self).__init__(*args, **kwargs)
