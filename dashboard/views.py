from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from dashboard.models import Ra
from django.core import serializers
from dashboard.forms import OrderForm

def dashboard_with_pivot(request):
    return render(request, 'ps.html', {})


def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:index')
    else:
        form = OrderForm()
    return render(request, 'add_order.html', {'form': form})

def index(request):
    orders = Ra.objects.all()
    return render(request, 'index.html', {'orders': orders})

def delete_order(request, order_id):
    order = get_object_or_404(Ra, pk=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('dashboard:index')
    return render(request, 'delete_order.html', {'order': order})

def home(request):
    return render(request, 'home.html', {})

def delte(request):
    orders = Ra.objects.all()
    return render(request, 'shr.html', {'orders': orders})
