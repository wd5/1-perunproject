from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import permission_required

from ftrainer.models import Exercise
from ftrainer.forms import ExerciseForm

@permission_required('ftrainer.add_exercise')
def exercise_list(request, published=True, part=None, member=None, skill=None,
        page=0, template_name='ftrainer/exercise_list.html', **kwargs):
    qs = Exercise.objects.select_related()
    if published:
        qs = qs.filter(is_published=True)
    else:
        qs = qs.filter(is_published=False)
    if part:
        qs = qs.filter(part__id=part)
    if member:
        qs = qs.filter(member__id=member)
    if skill:
        qs = qs.filter(skill__id=skill)
    return list_detail.object_list(
        request,
        queryset = qs,
        page = page,
        template_name = template_name,
        **kwargs)

@permission_required('ftrainer.add_exercise')
def exercise_detail(request, pk):
    exercise = Exercise.objects.get(id=pk)
    return direct_to_template(request, 'ftrainer/exercise_detail.html',
        {'exercise': exercise})

@permission_required('ftrainer.add_exercise')
def exercise_edit(request, pk=None):
    exercise = None
    if pk:
        exercise = Exercise.objects.get(id=pk)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            new_exercise = form.save(commit=False)
            new_exercise.user = request.user
            if 'publish' in request.POST:
                new_exercise.is_published = True
            if 'draft' in request.POST:
                new_exercise.is_published = False
            new_exercise.save()
            return HttpResponseRedirect(new_exercise.get_absolute_url())
    else:
        form = ExerciseForm(instance=exercise)

    return direct_to_template(request, 'ftrainer/exercise_edit.html',
        {'form':form, 'exercise':exercise})
