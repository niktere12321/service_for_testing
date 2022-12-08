from django import forms
from django.contrib.auth import get_user_model

from .models import Question

User = get_user_model()


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = "__all__"

    def clean(self):
        data = self.cleaned_data
        answers = data.get("choice_answer")
        one_true = None
        all_true_answer = None
        for get_answer in answers:
            if one_true is not None and all_true_answer is not None:
                break
            elif all_true_answer is None and get_answer.true_or_false is False:
                all_true_answer = True
            elif one_true is None and get_answer.true_or_false is True:
                one_true = True
        if one_true is None or all_true_answer is None:
            raise forms.ValidationError(
                "Должен быть хотябы 1 правильный вариант и все"
                " варианты не могут быть правильными"
            )
        return data
