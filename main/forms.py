from django import forms
from django.forms.widgets import NumberInput
from .models import IngredientesXxi



class IngredienteForm(forms.ModelForm):
    class Meta:
        model = IngredientesXxi
        fields = [
                'id_ingrediente',
                'ingrediente',
                'marca',
                'cantidad',
                
                
                
            ]
        labels = {
                'id_ingrediente':'id_ingrediente',
                'ingrediente':'ingrediente',
                'marca':'marca',
                'cantidad':'cantidad',
                
                
                
        }

class stockform(forms.ModelForm):
    class Meta:
        model = IngredientesXxi
        widgets = {
            'cantidad': NumberInput(attrs={'type': 'number',}),
        }

        fields = [
                'cantidad',
                
                
            ]
        
        labels = {
                'cantidad':'cantidad',
                
                
        }