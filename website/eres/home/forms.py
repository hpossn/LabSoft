from django import forms
from . import models
import GerenciadorEntregas
import GerenciadorFuncionarios


class CustomLoginForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ('username', 'password', )


class RegiaoForm(forms.ModelForm):
    class Meta:
        model = models.Regiao
        fields = ('nome', 'precoBase')

class ContactForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'

    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
            super(ContactForm, self).__init__(*args, **kwargs)
            self.fields['contact_name'].label = "Nome:"
            self.fields['contact_email'].label = "Email:"
            self.fields['content'].label = "Escreva aqui sua mensagem:"


class ClienteForm(forms.ModelForm):
    username = forms.CharField(required=True)
    class Meta:
        model = models.Cliente
        fields = ('nome', 'email', 'endereco', 'telefone', 'CNPJ', )


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = models.Veiculo
        fields = ('marca', 'modelo', 'ano', 'placa')


class EntregadorForm(forms.ModelForm):
    class Meta:
        model = models.Entregador
        fields = ('nome', 'dataNascimento', 'CPF', 'salario',)
        widgets = {
            'dataNascimento': forms.SelectDateWidget(years=range(1901,2016)),
        }


class ArquivoPedidosForm(forms.Form):
    # title = forms.CharField(max_length=256)
    file = forms.FileField()


class Rastreamento(forms.Form):
        codRastr = forms.CharField(required=True,
            widget= forms.TextInput(
                attrs={'class': 'form-control', 'id': 'codigoRatreamento', 'required': True}
            )
        )


class EntregaEntregadorForm(forms.Form):
    entrega_select = forms.ModelChoiceField(queryset=None)
    entregador_select = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super(EntregaEntregadorForm, self).__init__(*args, **kwargs)
        self.fields['entrega_select'].queryset = GerenciadorEntregas.listarPedidosPendentes()
        self.fields['entregador_select'].queryset = GerenciadorFuncionarios.listarEntregadoresDisponiveis()
        print(GerenciadorFuncionarios.listarEntregadoresDisponiveis())

class EntregasAlocadas(forms.Form):
    entrega_select = forms.ModelChoiceField(queryset=None)

    def __init__(self, idEntregador, *args, **kwargs):
        super(EntregasAlocadas, self).__init__(*args, **kwargs)
        self.fields['entrega_select'].queryset = GerenciadorEntregas.listarPedidosAlocados(idEntregador)
