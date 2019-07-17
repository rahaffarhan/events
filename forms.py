from django import forms
from .models import Event
from django.contrib.auth.models import User



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'event_name',
        ]

    def clean_event_name(self):
        event_name = self.cleaned_data.get('event_name')
        if event_name.lower() == 'abc':
            raise forms.ValidationError("not valid")
        return event_name


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('author',)


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]



