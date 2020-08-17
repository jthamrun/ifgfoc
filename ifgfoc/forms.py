from django.forms import ModelForm, Textarea
from django import forms
from .import models

class CreateConnectCard(ModelForm):

    class Meta:
        model = models.connectForm
        fields = '__all__'
        labels = {
            'firstName': 'First Name',
            'lastName': 'Last Name',
            'phoneNumber': 'Phone Number',
            'addressLine1': 'Address Line 1',
            'addressLine2': 'Address Line 2',
            'addressCity': 'City',
            'addressState': 'State',
            'addressZip': 'Zip Code',
            'addressCountry': 'Country',
            'addressBirthday': 'Birthday',
        }

class CreatePrayerCard(ModelForm):

    class Meta:
        model = models.prayerForm
        fields = '__all__'
        labels = {
            'firstName': 'First Name',
            'lastName': 'Last Name',
            'phoneNumber': 'Phone Number',
            'prayerRequests': 'Prayer Requests'
        }
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['prayerRequests'].widget.attrs.update({'cols': '80','rows':"80"})