from django import forms
from .models import Order

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class MakePaymentForm(forms.Form):
    
    # def __init__(self, *args, **kwargs):
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'paymentForm'
    #     self.helper.form_class = 'checkoutForms'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = 'checkout'
        
    #     super(MakePaymentForm, self).__init__(*args, **kwargs)
    
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2030)]
    
    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
    
    
    
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2',
            'county'
        )