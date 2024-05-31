from django.shortcuts import render

# hotel/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import RoomRate, OverriddenRoomRate, Discount
from .forms import RoomRateForm, OverriddenRoomRateForm, DiscountForm
# hotel/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import OverriddenRoomRate
from .forms import OverriddenRoomRateForm

from .models import Discount
from .forms import DiscountForm

# hotel/views.py

from django.shortcuts import render
from .models import RoomRate
from .utils import calculate_final_rate
from .forms import RoomRateForm

def lowest_rate_view(request):
    if request.method == "POST":
        form = RoomRateForm(request.POST)
        if form.is_valid():
            room_rate = form.cleaned_data['room_rate']
            stay_date = form.cleaned_data['stay_date']
            final_rate = calculate_final_rate(room_rate, stay_date)
            return render(request, 'templates/hotel/lowest_rate.html', {'final_rate': final_rate})
    else:
        form = RoomRateForm()
    return render(request, 'templates/hotel/lowest_rate_form.html', {'form': form})


# List all Room Rates
def room_rate_list(request):
    room_rates = RoomRate.objects.all()
    return render(request, 'templates/hotel/room_rate_list.html', {'room_rates': room_rates})


# Create a new Room Rate
def room_rate_create(request):
    if request.method == "POST":
        form = RoomRateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_rate_list')
    else:
        form = RoomRateForm()
    return render(request, 'templates/hotel/room_rate_form.html', {'form': form})


# Update an existing Room Rate
def room_rate_update(request, pk):
    room_rate = get_object_or_404(RoomRate, pk=pk)
    if request.method == "POST":
        form = RoomRateForm(request.POST, instance=room_rate)
        if form.is_valid():
            form.save()
            return redirect('room_rate_list')
    else:
        form = RoomRateForm(instance=room_rate)
    return render(request, 'templates/hotel/room_rate_form.html', {'form': form})


# Delete a Room Rate
def room_rate_delete(request, pk):
    room_rate = get_object_or_404(RoomRate, pk=pk)
    if request.method == "POST":
        room_rate.delete()
        return redirect('room_rate_list')
    return render(request, 'templates/hotel/room_rate_confirm_delete.html', {'room_rate': room_rate})




# List all Overridden Room Rates
def overridden_room_rate_list(request):
    overridden_rates = OverriddenRoomRate.objects.all()
    return render(request, 'templates/hotel/overridden_room_rate_list.html', {'overridden_rates': overridden_rates})


# Create a new Overridden Room Rate
def overridden_room_rate_create(request):
    if request.method == "POST":
        form = OverriddenRoomRateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('overridden_room_rate_list')
    else:
        form = OverriddenRoomRateForm()
    return render(request, 'templates/hotel/overridden_room_rate_form.html', {'form': form})


# Update an existing Overridden Room Rate
def overridden_room_rate_update(request, pk):
    overridden_rate = get_object_or_404(OverriddenRoomRate, pk=pk)
    if request.method == "POST":
        form = OverriddenRoomRateForm(request.POST, instance=overridden_rate)
        if form.is_valid():
            form.save()
            return redirect('overridden_room_rate_list')
    else:
        form = OverriddenRoomRateForm(instance=overridden_rate)
    return render(request, 'templates/hotel/overridden_room_rate_form.html', {'form': form})


# Delete an Overridden Room Rate
def overridden_room_rate_delete(request, pk):
    overridden_rate = get_object_or_404(OverriddenRoomRate, pk=pk)
    if request.method == "POST":
        overridden_rate.delete()
        return redirect('overridden_room_rate_list')
    return render(request, 'templates/hotel/overridden_room_rate_confirm_delete.html', {'overridden_rate': overridden_rate})


# List all Discounts
def discount_list(request):
    discounts = Discount.objects.all()
    return render(request, 'templates/hotel/discount_list.html', {'discounts': discounts})

# Create a new Discount
def discount_create(request):
    if request.method == "POST":
        form = DiscountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discount_list')
    else:
        form = DiscountForm()
    return render(request, 'templates/hotel/discount_form.html', {'form': form})

# Update an existing Discount
def discount_update(request, pk):
    discount = get_object_or_404(Discount, pk=pk)
    if request.method == "POST":
        form = DiscountForm(request.POST, instance=discount)
        if form.is_valid():
            form.save()
            return redirect('discount_list')
    else:
        form = DiscountForm(instance=discount)
    return render(request, 'templates/hotel/discount_form.html', {'form': form})

# Delete a Discount
def discount_delete(request, pk):
    discount = get_object_or_404(Discount, pk=pk)
    if request.method == "POST":
        discount.delete()
        return redirect('discount_list')
    return render(request, 'templates/hotel/discount_confirm_delete.html', {'discount': discount})