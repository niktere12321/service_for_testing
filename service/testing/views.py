from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Test, TestTasks

User = get_user_model()


class Index(generic.ListView):
    """Просмотр всех тестов"""
    model = Test
    paginate_by = 10
    template_name = 'testing/index.html'

    def get_queryset(self):
        self.filter = self.request.GET.get("filter")
        if self.filter and self.filter == "passed":
            queryset = TestTasks.objects.filter(user=self.request.user)
        else:
            queryset = Test.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.filter:
            context["filter"] = "True"
        return context


class GetResult(generic.DetailView):
    """Просмотр пройденного теста"""
    model = TestTasks
    template_name = 'testing/get_result.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_now = self.object
        context["procent"] = object_now.true_in_test / object_now.all_point_test * 100
        context["fasle_answer"] = object_now.all_point_test - object_now.true_in_test
        return context


@login_required
def testing(request):
    test = Test.objects.get(pk=request.GET.get('id'))
    questions = test.question.all()
    if request.POST:
        count_all = 0
        count_true = 0
        choice_answer = []
        for question in questions:
            choice = question.choice_answer.all()
            for answer in choice:
                choice_answer.append(answer)
        data = []
        for key in dict(request.POST):
            if key == 'csrfmiddlewaretoken':
                continue
            data_key = key.split('-')
            data.append((data_key[0], data_key[1],))
        for answer in data:
            if get_object_or_404(Choice, pk=int(answer[1])).true_or_false is True:
                count_true += 1
            count_all += 1
        test_tasks = TestTasks()
        test_tasks.test = test
        test_tasks.user = request.user
        test_tasks.true_in_test = count_true
        test_tasks.all_point_test = count_all
        test_tasks.save()
        return redirect(reverse('testing:get_result', args=[test_tasks.pk]))
    context = {'questions': questions}
    return render(request, 'testing/testing.html', context)
