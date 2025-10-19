from django.shortcuts import render, redirect
from django.contrib import messages
from item.models import Item, Catagory
# Create your views here.
from .forms import SignUpForm

def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[:6]
    categories = Catagory.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings  # to use EMAIL_HOST_USER

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Compose email content
        subject = f"New Contact Message from {name}"
        message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        recipient_list = ['haleluyatigabe1990@gmail.com']  

        try:
            send_mail(
                subject,
                message_body,
                settings.EMAIL_HOST_USER,  
                recipient_list,
                fail_silently=False,
            )
            messages.success(request, 'Thank you! Your message has been sent.')
        except Exception as e:
            messages.error(request, f"Oops! Something went wrong: {e}")

        return redirect('core:contact')

    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # You might want to log the user in and redirect to a success page
            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})