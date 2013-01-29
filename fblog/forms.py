from django import forms
from fblog.models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('author', 'preview')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('save', 'Save and publish'))
        self.helper.add_input(Submit('draft', 'Save to draft'))
        self.helper.layout = Layout(
            Fieldset(
                'first arg is the legend of the fieldset',
                'title',
                'slug',
                'content',
            ),
            Fieldset(
                'Publication',
                'date',
                'type',
                'related_entries',
                'is_featured',
                'enable_comments',
            ),
            Fieldset(
                'Meta',
                'meta_title',
                'meta_description',
                'meta_keywords',
            )
        )
        super(PostForm, self).__init__(*args, **kwargs)
        #self.fields['category'].widget.attrs['style'] = 'width: 98%'
        #self.fields['title'].widget.attrs['style'] = 'width: 98%'
        #self.fields['slug'].widget.attrs['style'] = 'width: 98%'
        #self.fields['content'].widget.attrs['cols'] = 80
        #self.fields['content'].widget.attrs['rows'] = 16
        #self.fields['content'].widget.attrs['style'] = 'width: 98%'
        #self.fields['related_entries'].widget.attrs['style'] = 'width: 98%'
