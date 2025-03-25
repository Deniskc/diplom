from django import forms


from main.models import Students, Settings


class RequestEducationForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = [
            'first_name',
            'last_name',
            'surname',
            'birth_date',
            'email',
            'phone',
            'curse',
        ]

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = [
            'theme',
        ]
    