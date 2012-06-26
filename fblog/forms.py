from django import forms
from fblog.models import Post
from django.contrib.admin.widgets import FilteredSelectMultiple

class PostForm(forms.ModelForm):
    related_entries = forms.ModelMultipleChoiceField(
            queryset=Post.objects.all(),
            widget=FilteredSelectMultiple("verbose name", is_stacked=False),
            required=False)

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
