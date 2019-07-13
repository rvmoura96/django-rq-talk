from django.shortcuts import render, redirect
from django.views.generic import ListView

from core.models import FibNumber
from .forms import FibNumberForm
from .tasks import fib_assinc


def home(request):
    return render(request, "core/index.html")


class FibNumberListView(ListView):
    model = FibNumber
    template_name = "core/index.html"


def fib_create(request):
    if request.method == "POST":
        form = FibNumberForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            fibonacci_number = form.save(commit=False)
            fib_assinc(fibonacci_number)
        return redirect("home")
    form = FibNumberForm()
    context = {"form": form}
    return render(request, "core/form.html", context)
