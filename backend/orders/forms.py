from django import forms
from .models import Order, OrderItem
# external admin form start

class AddOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddOrderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
              
    class Meta:
        model = Order
        fields = ('first_name','last_name','email','address','zipcode','phone','place','paid_amount')

class EditOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditOrderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control' 
    class Meta:
        model = Order
        fields = ('first_name','last_name','email','address','zipcode','phone','place','paid_amount')


class AddOrderItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddOrderItemForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
              
    class Meta:
        model = OrderItem
        fields = ('product','price','quantity',)