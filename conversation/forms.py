from django import forms 
from . models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={
                'placeholder': 'Type a message...',
                'class': 'flex-1 px-4 py-2 border rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500'
            })
        }