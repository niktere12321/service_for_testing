from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Choice(models.Model):
    title = models.CharField('Вариант ответа', max_length=4096)
    true_or_false = models.BooleanField(
        'Праильный ответ или нет',
        default=False
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'

    def __str__(self):
        return f'{self.title} от {self.pub_date.strftime("%d.%m.%Y")}'


class Question(models.Model):
    choice_answer = models.ManyToManyField(Choice)
    title = models.CharField('Задание', max_length=4096)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return f'{self.title} от {self.pub_date.strftime("%d.%m.%Y")}'


class Test(models.Model):
    question = models.ManyToManyField(Question)
    title = models.CharField('Текст теста', max_length=4096)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return f'{self.title} от {self.pub_date.strftime("%d.%m.%Y")}'


class TestTasks(models.Model):
    test = models.ForeignKey(Test, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    true_in_test = models.IntegerField()
    all_point_test = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Выполненое задание'
        verbose_name_plural = 'Выполненые задания'

    def __str__(self):
        return f'{self.test.title} от {self.pub_date.strftime("%d.%m.%Y")}'