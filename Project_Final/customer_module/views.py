from django.utils import timezone
from .models import Order
from django.shortcuts import render, get_object_or_404
from .forms import OrderForm
from django.shortcuts import redirect


def Order_list(request):
    Orders = Order.objects.filter(Order_date__lte=timezone.now()).order_by("Order_date")
    return render(request, "customer_module/Order_list.html", {"Orders": Orders})

def Order_detail(request, pk):
    Order = get_object_or_404(request, pk=pk)
    return render(request, "customer_module/Order_detail.html", {"Order": Order})

def Order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            Order = form.save(commit=False)
            Order.Customer = request.user
            Order.Order_date = timezone.now()
            Order.save()
            return redirect("Order_detail", pk=request.pk)
    else:
        form = OrderForm()
    return render(request, "customer_module/Order_edit.html", {"form": form})

def Order_edit(request, pk):
    Order = get_object_or_404(request, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=Order)
        if form.is_valid():
            Order = form.save(commit=False)
            Order.Customer = request.user
            Order.Order_date = timezone.now()
            Order.save()
            return redirect("Order_detail", pk=request.pk)
    else:
        form = OrderForm(instance=Order)
    return render(request, "customer_module/Order_edit.html", {"form": form})
