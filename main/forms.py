from django import forms


from main.models import Students


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
        ]

    first_name = forms.CharField()
    last_name = forms.CharField()
    surname = forms.CharField()
    birth_date = forms.DateField()
    email = forms.EmailField()
    phone = forms.IntegerField()
