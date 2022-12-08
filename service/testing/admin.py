from django.contrib import admin

from .forms import QuestionForm
from .models import Question, Choice, Test, TestTasks


class TestAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'pub_date',
    )


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    list_display = (
        'pk',
        'title',
        'pub_date',
    )


class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'true_or_false',
        'pub_date',
    )


class TestTasksAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'test',
        'user',
        'pub_date',
    )
    list_filter = ('user', 'test',)


admin.site.register(TestTasks, TestTasksAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
