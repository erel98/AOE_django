from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UserForm


# Create your views here.
def index(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            success(request='GET')
    context = {'form': form}
    return render(request, 'form/index.html', context)


def success(request):
    return render(request, 'form/success.html')
