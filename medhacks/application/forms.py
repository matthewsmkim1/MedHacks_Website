from django import forms
from application.models import ApplicationModel

class ApplicationForm(forms.ModelForm):
    text = forms.CharField()

    class Meta:
        model = ApplicationModel

        #Remember to leave a comma at the end
        fields = ('text',)
