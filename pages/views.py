from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ContactForm, ContactModelForm
from .models import Contact

from blog.models import Article

# Create your views here.
def home(request):
    articles = Article.objects.all()

    context = {'articles': articles,  }
    return render(request, 'pages/home.html', context)


def sidbar(request):
    recent_articles = Article.objects.order_by('-created_date')[:3]
    context = {'recent': recent_articles}
    return render(request, 'partial/side_bar.html', context)



def contact_us(request):

    if request.method == "POST":
        # form = ContactForm(request.POST)
        form = ContactModelForm(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            # Contact.objects.create(name=cd['name'], email=cd['email'], subject=cd['subject'], message=cd['message'])
            # messages.success(request, 'Your message successfully sent')
            # return redirect('contact')
            form.save()
            messages.success(request, 'Your message successfully sent')
            return redirect('contact')

        return render(request, 'pages/contact_us.html', {'form':form})
    


    form = ContactForm()
    return render(request, 'pages/contact_us.html', {'form': form})