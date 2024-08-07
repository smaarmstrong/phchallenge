from django.shortcuts import render, redirect
from .models import EnclosureModel
from .forms import EnclosureForm

def check_planning_permission(location, height, constraint):
    location = 'na' if location == 'not_applicable' else location
    height = 'na' if height == 'not_applicable' else height
    constraint = 'na' if constraint == 'not_applicable' else constraint

    if constraint != 'na':
        return "Permission needed"
    if location == 'na' and height == 'na':
        return "No permission needed"
    if location == 'na' and height == 'above_2m':
        return "Permission needed"
    if location == 'adjacent_vehicular_highway' and height == 'up_to_1m':
        return "No permission needed"
    elif location == 'adjacent_vehicular_highway' and height in ['above_1m', 'up_to_2m', 'above_2m']:
        return "Permission needed"
    elif location == 'facing_listed_building':
        return "Permission needed"
    return "No permission needed"

def check_enclosure(request):
    if request.method == "POST":
        form = EnclosureForm(request.POST)
        if form.is_valid():
            enclosure = form.save(commit=False)
            enclosure.permission_status = check_planning_permission(enclosure.location, enclosure.height, enclosure.constraint)
            enclosure.save()
            return redirect('check_enclosure')  # Redirect to the same view to update the table
    else:
        form = EnclosureForm()
    enclosures = EnclosureModel.objects.all().order_by('-id')
    return render(request, 'check_enclosure.html', {'form': form, 'enclosures': enclosures})

def clear_enclosures(request):
    EnclosureModel.objects.all().delete()
    return redirect('check_enclosure')

def enclosure_list(request):
    enclosures = EnclosureModel.objects.all().order_by('-id')
    return render(request, 'enclosure_list.html', {'enclosures': enclosures})