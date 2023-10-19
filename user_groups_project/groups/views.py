from django.shortcuts import render

# groups/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Group
from .forms import GroupForm

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups/group_list.html', {'groups': groups})

def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'groups/group_form.html', {'form': form})

def edit_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'groups/group_form.html', {'form': form, 'group': group})

def delete_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if group.can_delete:
        group.delete()
    return redirect('group_list')

