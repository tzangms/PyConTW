from django.shortcuts import get_object_or_404, render
from django.contrib.admin.views.decorators import staff_member_required

from boxes.forms import BoxForm
from boxes.models import Box


@staff_member_required
def box_edit(request, pk):
    box = get_object_or_404(Box, pk=pk)

    form = BoxForm(request.POST or None, instance=box)
    if form.is_valid():
        form.save()
        return render(request, "boxes/refresh.html")

    return render(request, "boxes/box_edit.html", {'form': form, 'box': box})


@staff_member_required
def box_create(request, label):

    form = BoxForm(request.POST or None)
    if form.is_valid():
        box = form.save(commit=False)
        box.label = label
        box.created_by = request.user
        box.language_code = request.LANGUAGE_CODE
        box.last_updated_by = request.user
        box.save()

        return render(request, "boxes/refresh.html")

    return render(request, "boxes/box_create.html", {'form': form, 'label': label})
