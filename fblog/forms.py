from django import forms
from fblog.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('author', 'preview')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        #self.fields['category'].widget.attrs['style'] = 'width: 98%'
        #self.fields['title'].widget.attrs['style'] = 'width: 98%'
        #self.fields['slug'].widget.attrs['style'] = 'width: 98%'
        #self.fields['content'].widget.attrs['cols'] = 80
        #self.fields['content'].widget.attrs['rows'] = 16
        #self.fields['content'].widget.attrs['style'] = 'width: 98%'
        #self.fields['related_entries'].widget.attrs['style'] = 'width: 98%'
