from django import forms
from.models import Post, Reply

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content","image","title","tags"]
        widgets = {
            "content" : forms.Textarea(attrs={
                'rows':4,
                'cols':40, 
                'Placeholder' :'Write a content',
                'class':'content'
                }),
            
            "title" : forms.TextInput(attrs={
                'placeholder':'Questions,Doubts,Funny,Quiz', 
                'class':'title'
                }),
            
            "tags":forms.TextInput(attrs={
                'placeholder':'tags',
                'class':'tags'
                })
        }
        help_texts = {
            'content': 'Write content here.',
            'title': 'Questions, Doubts, Funny, Quiz',
            'tags': 'Add relevant tags for your post.'
        }
       
       
class ReplyForm(forms.ModelForm):
    class Meta :
        model = Reply
        fields = ["comment"]
        widgets = {
            "comment" : forms.Textarea(attrs={
                'rows':3,
                'help_text': 'Write your reply',
                'class' : 'comments'
            })
        } 
        