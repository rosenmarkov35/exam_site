from django import forms

from exam_site.second_hand.models import SecondHandProduct


class SecondHandSellForm(forms.ModelForm):
    class Meta:
        model = SecondHandProduct
        fields = ('second_hand_product_name', 'second_hand_product_image', 'second_hand_product_price',
                  'second_hand_product_description')

        widgets = {
            'second_hand_product_name': forms.TextInput(
                attrs={'placeholder': 'Name of the item that you want to sell'}),
            'second_hand_product_image': forms.DateInput(attrs={'placeholder': 'dd/mm/yyyy', 'type': 'date'}),
            'pet_photo': forms.TextInput(attrs={'placeholder': 'Link to image'}),
        }

        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'pet_photo': 'Link to Image',
        }
