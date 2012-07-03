from django import forms
from fblog.models import Post
from selectable.forms import AutoCompleteWidget
from selectable.forms import AutoCompleteSelectField
from selectable.forms import AutoComboboxSelectWidget
from fblog.lookups import CategoryLookup

class PostForm(forms.ModelForm):

    autocompleteselect = AutoCompleteSelectField(
        widget = AutoComboboxSelectWidget,
        lookup_class=CategoryLookup,
        label='Select a fruit (AutoCompleteField)',
        required=False,
    )

    class Meta:
        model = Post
        exclude = ('author')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        #self.fields['category'].widget.attrs['style'] = 'width: 98%'
        #self.fields['title'].widget.attrs['style'] = 'width: 98%'
        #self.fields['slug'].widget.attrs['style'] = 'width: 98%'
        #self.fields['content'].widget.attrs['cols'] = 80
        #self.fields['content'].widget.attrs['rows'] = 16
        #self.fields['content'].widget.attrs['style'] = 'width: 98%'
        #self.fields['related_entries'].widget.attrs['style'] = 'width: 98%'
