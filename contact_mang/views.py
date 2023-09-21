from django.shortcuts import render, redirect

from .models import Contact
from .forms import ContactForm

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})
def contact_list(request):
    contacts = Contact.objects.all()

    if request.method == 'POST':
        contact_id = request.POST.get('contact_id')
        contact = Contact.objects.get(id=contact_id)
        form = ContactForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            # Refresh the contact list after saving changes
            contacts = Contact.objects.all()  # Get the updated list of contacts
            return redirect('contact_list')

    else:
        form = ContactForm()

    return render(request, 'contact_list.html', {'contacts': contacts, 'form': form})
