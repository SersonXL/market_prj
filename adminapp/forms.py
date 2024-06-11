from django import forms
from authapp.models import TravelUser
from authapp.forms import TravelUserEditForm
from mainapp.models import ListOfCountries
from mainapp.models import Regions
from mainapp.models import Accommodation
from ordersapp.models import Order



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()


# Форма редактирования параметров пользователя
class TravelUserAdminEditForm(TravelUserEditForm):
    class Meta:
        model = TravelUser
        fields = '__all__'


# Форма редактирования параметров стран
class ListOfCountriesEditForm(forms.ModelForm):
    class Meta:
        model = ListOfCountries
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class RegionsEditForm(forms.ModelForm):
    class Meta:
        model = Regions
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


# Форма редактирования параметров услуг компании
class AccommodationEditForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
