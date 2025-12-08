
from django import forms

from .models import Topic, Entry, TodoList

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['topic', 'text']
        labels = {'topic': '', 'text': ''}
