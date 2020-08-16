from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm

def index(request):
    return render(request, "disha.html")

def customer_entry(request):
    # if this is a POST request we need to process the form data
    template = 'disha.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data["name"])
            print(form.cleaned_data["mobile_no"])
            print(form.cleaned_data["message"])
            form.save()
            form = CustomerForm()

            # Login the user
            # login(request, user)

            # redirect to accounts page:
            # return HttpResponseRedirect('/')

        else:
            return render(request, template, {'form': form})

    # No post data availabe, let's just show the page.
    else:
        form = CustomerForm()

    return render(request, template, {'form': form})