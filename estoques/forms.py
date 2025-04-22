from django import forms
from .models import Estoque

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['produto', 'quantidade_disponivel', 'valor_unitario', 'categoria', 'validade', 'raridade']
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}),
        }