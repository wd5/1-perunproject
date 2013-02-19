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
        self.helper.add_input(Submit('save', _('Save')))
        #self.helper.add_input(Submit('draft', 'Save to draft'))
        self.helper.layout = Layout(
            Div(
                #'Content',
                'title',
                'part',
                'member',
                'skill',
                'content',
                'enable_comments',
                'is_published',
            ),
        )
        super(ExerciseForm, self).__init__(*args, **kwargs)
