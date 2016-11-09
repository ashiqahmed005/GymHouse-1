from django import forms
from django.forms import ModelForm
from mainpage.models import Event
from mainpage.models import Class

class NewEventForm(ModelForm):
    class Meta:
        model = Event
        #fields = '__all__'
        exclude = ['creator']

        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})}
        """
        labels = {
            'name': _('Event name'),
            'description': _('Event description'),
            'date': _('Date of the event'),
            'participants': _('Participants'),
            'trainer': _('Trainer for the event'),
            'level': _('Exercise level'),
        }
        help_texts = {
            'name': _('Event name will be shown in the calendar'),
        }
        
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }
        
        """


class NewClassForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewClassForm, self).__init__(*args, **kwargs)
        self.fields['days'].empty_label = None
    class Meta:
        model = Class
        exclude = ['creator']
        #'time': forms.TimeInput(format='%H:00'),
        widgets = {
                'begin_date': forms.DateInput(attrs={'class': 'datepicker'}),
                'end_date': forms.DateInput(attrs={'class': 'datepicker'}),
                'days': forms.CheckboxSelectMultiple()
        }


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
