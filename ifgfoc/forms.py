from django.forms import ModelForm
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