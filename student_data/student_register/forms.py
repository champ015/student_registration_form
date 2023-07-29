from django import forms
from .models import employee
class studentform(forms.ModelForm):
    class Meta:
        model=employee
        fields="__all__"
    def __init__(self,*args,**kwrgs):
        super(studentform,self).__init__(*args,**kwrgs)
        self.fields['position'].empty_label='select option'
        self.fields['studcode'].required=False
    
        
