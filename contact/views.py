from django.shortcuts import render
from .forms import ContactForm
from .models import Message

# Create your views here.

def contact(req):
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            Message.objects.create(**data)
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(req, 'contact.html', context)
