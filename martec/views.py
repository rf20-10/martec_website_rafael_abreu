from django.shortcuts import render, redirect
from django import forms
from .models import Products, Contact_Form
from django. contrib import messages

def index(request):
    return render(request, 'martec/index.html')

def products(request):
    # Retrieving all products using .all().
    all_products = Products.objects.all()
    return render(request, 'martec/products.html', {'products': all_products})

def about_us(request):
    return render(request, 'martec/about_us.html')

def contact(request):
    class ContactForm(forms.ModelForm):
        class Meta:
            model = Contact_Form
            # Creating form fields.
            fields = ['first_name', 'last_name', 'email', 'phone', 'message']
            # Creating labels so the fields will be displayed in Portuguese.
            labels = {'first_name': 'Nome', 'last_name': 'Sobrenome', 'email': 'Email', 'phone': 'Telefone', 'message': 'Mensagem'}
            widgets = {
                'first_name': forms.TextInput(attrs={'class':'form-control'}),
                'last_name': forms.TextInput(attrs={'class':'form-control'}),
                'email': forms.EmailInput(attrs={'class':'form-control'}),
                'phone': forms.TextInput(attrs={'class':'form-control'}),
                'message': forms.Textarea(attrs={'class':'form-control', 'rows': 5}),
            }
            # Indicating exactly what went wrong when submitting the form and ecountering errors.
            error_messages = {
                'first_name': {
                    'required': 'Informe seu nome',
                }, 
                'last_name': {
                    'required': 'Informe seu sobrenome',
                },
                'email': {
                    'required': 'Informe seu email',
                    'invalid': 'Informe um email válido', 
                },
                'phone': {
                    'required': 'Informe seu telefone',
                }
            }

    form = ContactForm(request.POST or None)
    status = None
    if request.method == 'POST':
        # Form validation if-statement.
        if form.is_valid():
            form.save()
            status = 'success'
        else:
            status = 'error'
        
    return render(request, 'martec/contact.html', {'form': form, 'form_status': status})        