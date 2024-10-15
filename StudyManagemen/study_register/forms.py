from django import forms
from .models import Study

class Studyform(forms.ModelForm):
    STUDY_PHASE_CHOICES = [
        ('Phase 1', 'Phase 1'),
        ('Phase 2', 'Phase 2'),
        ('Phase 3', 'Phase 3'),
        ('Phase 4', 'Phase 4'),
    ]

    # Adding custom styling for 'studyphase' select field
    studyphase = forms.ChoiceField(
        choices=STUDY_PHASE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',  # Bootstrap class
            'id': 'study-phase-select',  # Custom ID
        }),
        label='Study Phase',
    )

    # Adding datalist feature for 'sponsorname' with custom styles
    sponsorname = forms.CharField(
        widget=forms.TextInput(attrs={
            'list': 'sponsorname-list',
            'class': 'form-control',  # Bootstrap class for styling
            'placeholder': 'Enter or select a sponsor name',  # Placeholder text
        }),
        label='Sponsor Name',
    )

    class Meta:
        model = Study
        fields = ('studyname', 'studyphase', 'studydescription', 'sponsorname')
        labels = {
            'studyname': 'Study Name',
            'studydescription': 'Study Description',
        }

        # Applying custom widgets to Meta fields
        widgets = {
            'studyname': forms.TextInput(attrs={
                'class': 'form-control',  # Styling for study name
                'placeholder': 'Enter study name',  # Placeholder text
            }),
            'studydescription': forms.Textarea(attrs={
                'class': 'form-control',  # Styling for description
                'rows': 3,  # Number of rows for the textarea
                'placeholder': 'Enter study description',
            }),
        }
